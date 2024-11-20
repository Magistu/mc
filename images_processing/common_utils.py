import numpy as np
import os
from typing import Union
from PIL import Image
from PIL.Image import Image as PILImage


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


def convert_to_png(data, opacity=True):
    return np.array(as_PilImg(data).convert('RGBA' if opacity else 'RGB'))


def all_from_dir(dir, format='png'):
    return (e.split('.')[0] for e in os.listdir(dir) if e.split('.')[-1] == format)