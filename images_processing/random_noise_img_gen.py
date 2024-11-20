import random

from PIL import Image
import numpy as np

results_dir = "new_images"


def get_palette(path):
    palette = np.array(Image.open(path))
    return palette.reshape(palette.shape[1], palette.shape[2])


def add_noise(image, palette, amount=1.0):
    if 0.0 > amount > 1.0:
        raise ValueError("Amount must be in range from zero to one")
    output = np.copy(np.array(image))
    size = output.shape[0] * output.shape[1]
    n = int(amount * size)
    coords = np.array(random.sample([(i, j) for i in range(output.shape[0]) for j in range(output.shape[1])], n))
    for y, x in coords:
        output[y, x] = palette[np.random.randint(0, len(palette))]
    return Image.fromarray(output)


def main():
    rust = get_palette("images_processing/palette/rust_palette.png")

    width = 128
    height = 64

    image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
    new_image = add_noise(image, rust)
    new_image.save(results_dir + "/noise.png")


if __name__ == "__main__":
    main()
