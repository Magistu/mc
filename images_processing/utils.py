import os
from typing import Union
from PIL import Image
from PIL.Image import Image as PILImage
import numpy as np
import colorsys

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)


def as_PilImg(data: Union[bytes, PILImage, np.ndarray]):
    if isinstance(data, PILImage):
        return data
    elif isinstance(data, np.ndarray):
        return Image.fromarray(data)
    else:
        raise ValueError("Input type {} is not supported.".format(type(data)))


def as_NdArray(data: Union[bytes, PILImage, np.ndarray], dtype=None):
    if isinstance(data, PILImage):
        return np.array(data, dtype)
    elif isinstance(data, np.ndarray):
        return data if dtype is None else data.astype(dtype)
    else:
        raise ValueError("Input type {} is not supported.".format(type(data)))


def select(data, x, y, size_x, size_y):
    return as_NdArray(data)[y:y + size_y, x:x + size_x, :]


def clear_area(data, x, y, size_x, size_y):
    data = as_NdArray(data)
    data[y:y + size_y, x:x + size_x, 3] = 0
    return data


def paste(bg_data, fg_data, x, y):
    bg_data = as_PilImg(bg_data)
    fg_data = as_PilImg(fg_data)
    bg_data.paste(fg_data, (x, y))
    return bg_data


def trans_paste(bg_data, fg_data, x, y):
    bg_data = as_PilImg(bg_data)
    fg_data = as_PilImg(fg_data)
    fg_data_trans = Image.new("RGBA", bg_data.size)
    fg_data_trans.paste(fg_data, (x, y), mask=fg_data)
    return Image.alpha_composite(bg_data, fg_data_trans)


def copypaste_area(data_to, data_from, x0, y0, size_x, size_y, x1, y1):
    return trans_paste(as_NdArray(data_to), select(as_NdArray(data_from), x0, y0, size_x, size_y), x1, y1)


def copypaste(data, x0, y0, size_x, size_y, x1, y1):
    return copypaste_area(as_NdArray(data), as_NdArray(data).copy(), x0, y0, size_x, size_y, x1, y1)


def copypaste_image(data, path, x0, y0, size_x, size_y, x1, y1):
    return copypaste_area(as_NdArray(data), np.array(Image.open(path)), x0, y0, size_x, size_y, x1, y1)


def displace(data, x0, y0, size_x, size_y, x1, y1):
    data = as_NdArray(data)
    area = select(data, x0, y0, size_x, size_y)
    return paste(clear_area(data, area), area, x1, y1)


def pick_color(data, position):
    return as_NdArray(data)[position[1], position[0], :]


def convert_to_png(data):
    return np.array(as_PilImg(data).convert('RGBA'))


# def flip_vertically(data, x, y, size_x, size_y):
#     area = select(data, x, y, size_x, size_y)
#     area.flip_vertically()
#     data = paste(data, area, x, y)
#     return data


# def flip_horizontally(data, x0, y0, size_x, size_y):
#     area = select(data, x0, y0, size_x, size_y)
#     area.flip_horizontally()
#     data = paste(data, area, x0, y0)
#     return data


def paint(data1, positions, lambda_color):
    data = as_NdArray(data1).copy()
    for position in positions:
        data[position[1], position[0], :] = lambda_color(data1)
    return data


def resize_canvas(data, size_x, size_y):
    return as_NdArray(data)[:size_y, :size_x, :]


def resize(data, size_x, size_y):
    return np.array(as_PilImg(data).resize((size_x, size_y)))


def crop(data, x0, y0, x1, y1):
    return as_NdArray(data)[y0:y1, x0:x1, :]


def apply_allocation(data, path):
    data = np.minimum(as_NdArray(data), np.array(Image.open(path)))
    return data


def clear_allocation(data, path):
    data = as_NdArray(data)
    opacity = np.minimum(data[:, :, 3], 255 - np.array(Image.open(path))[:, :, 3])
    data[:, :, 3] = opacity
    return data


def get_channel(data, index):
    return as_NdArray(data)[:, :, index]


def set_channel(data, channel, indices):
    data = as_NdArray(data)
    data[:, :, indices] = channel
    return data


def set_channel_from_path(data, index_from, indices_to, path):
    return set_channel(as_NdArray(data), get_channel(np.array(Image.open(path)), index_from), indices_to)


def relocate_channel(data, index_from, indices_to):
    return set_channel(as_NdArray(data), get_channel(data, index_from), indices_to)


def invert_channels(data, indices):
    data = as_NdArray(data)
    for index in indices:
        data[:, :, index] = 255 - data[:, :, index]
    return data


def round_up_channel(data, index, threshold):
    data = as_NdArray(data)
    if data[:, :, index] > threshold:
        data[:, :, index] = 255
    return data


def round_down_channel(data, index, threshold):

    def f(ele):
        if ele[index] < threshold:
            ele[index] = 0
        return ele

    return np.apply_along_axis(f, 2, as_NdArray(data))


def set_hue(data, hue):
    r, g, b, a = np.rollaxis(as_NdArray(data), axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    r, g, b = hsv_to_rgb(hue, s, v)
    return np.dstack((r, g, b, a))


def set_saturation(data, saturation):
    r, g, b, a = np.rollaxis(as_NdArray(data), axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    r, g, b = hsv_to_rgb(h, saturation, 255.0 * np.sqrt(v / 255.0))
    return np.dstack((r, g, b, a))


def dye(data, r, g, b):
    img = as_NdArray(data, dtype=np.cfloat)
    img[:, :, 0] *= r / 255.0
    img[:, :, 1] *= g / 255.0
    img[:, :, 2] *= b / 255.0
    return img.astype(np.uint8)


def remove_background(data):
    import rembg
    return rembg.remove(data)


def all_from_dir(dir, format='png'):
    return (e.split('.')[0] for e in os.listdir(dir) if e.split('.')[-1] == format)