import numpy as np
import torch
from torch import nn
from PIL import Image
from common_utils import convert_to_png
from nn_helper import get_device, train, argmax_metric, predict
from paths import *


device = get_device()
replacer_cache = {}


class PaletteReplacer:
    def __init__(self, source_material):
        self.source_material = source_material
        self.source_palette = Image.open(palettes_dir + '/' + source_material + '_palette.png')
        self.palette_size = np.array(self.source_palette).shape[1]
        source_pal = np.array(self.source_palette, dtype=float)[:, :, :3].reshape(self.palette_size, 3) / 255
        self.qualifier = create_qualifier(source_pal)


def mix(ratio, pal, pal_size):
    return (ratio * pal)[:pal_size].sum(0)


def redistribute_colors(layer, distribution, pal):
    layer[:, :, :3] = (np.expand_dims(distribution, axis=3) * pal).sum(2)
    return layer


def get_color_distribution(layer, qualifier, pal_size):
    distribution = np.zeros((layer.shape[0], layer.shape[1], pal_size))
    visible_mask = layer[:, :, 3] != 0
    distribution[visible_mask] = predict(qualifier, torch.tensor(layer[visible_mask][:, :3] / 255, dtype=torch.float32), device)
    return distribution


def to_categorical(y, num_classes=None, dtype='float32'):
    y = np.array(y, dtype='int')
    input_shape = y.shape
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])
    y = y.ravel()
    if not num_classes:
        num_classes = np.max(y) + 1
    n = y.shape[0]
    categorical = np.zeros((n, num_classes), dtype=dtype)
    categorical[np.arange(n), y] = 1
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    return categorical


def create_qualifier(source_pal: np.ndarray):
    pal_size = source_pal.shape[0]
    qualifier = nn.Sequential(nn.Linear(3, pal_size * 10), nn.ReLU(), nn.Linear(pal_size * 10, pal_size * 10), nn.ReLU(), nn.Linear(pal_size * 10, pal_size), nn.Softmax())
    data = tuple(zip(source_pal.astype('float32'), to_categorical(range(pal_size))))
    print(qualifier)
    train_dataloader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=True)
    val_dataloader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False)
    learning_rate = 0.001
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(qualifier.parameters(), lr=learning_rate)
    epochs = 250
    train(qualifier, loss_fn, optimizer, train_dataloader, val_dataloader, epochs, argmax_metric, device, logging_period=8)
    return qualifier


def get_palette(image, pal_size):
    palette = image.convert('RGBA').convert(mode='P', dither='NONE', colors=pal_size)
    return np.reshape(np.array(palette.getpalette()[:3 * pal_size]).astype(np.uint8), (1, pal_size, 3))


def replace_palette(data, source_material, new_material):
    if source_material not in replacer_cache:
        replacer_cache[source_material] = PaletteReplacer(source_material)
    replacer = replacer_cache[source_material]
    color_distribution = get_color_distribution(data, replacer.qualifier, replacer.palette_size)
    new_pal = convert_to_png(Image.open(palettes_dir + '/' + new_material + '_palette.png'), False)
    new_pal = new_pal.reshape(replacer.palette_size, 3)
    return redistribute_colors(data, color_distribution, new_pal)
