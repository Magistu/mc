from utils import *
from paths import *
from batch_processing import execute_for_batch


# color_variants = {
#     "orange": (216, 127, 51),
#     "magenta": (178, 76, 216),
#     "light_blue": (102, 153, 216),
#     "yellow": (229, 229, 51),
#     "lime": (127, 204, 25),
#     "pink": (242, 127, 165),
#     "gray": (76, 76, 76),
#     "light_gray": (153, 153, 153),
#     "cyan": (76, 127, 153),
#     "purple": (127, 63, 178),
#     "blue": (51, 76, 178),
#     "brown": (102, 76, 51),
#     "green": (102, 127, 51),
#     "red": (153, 51, 51),
#     "black": (25, 25, 25),
#     "white": (255, 255, 255),
# }

color_variants = {
    "": (255, 132, 173)
}


def colored_name(name, colname):
    return name.replace("white", colname) if colname in name else f"{colname}_{name}"


def main():
    for colname, (r, g, b) in color_variants.items():
        execute_for_batch(images_dir, ((convert_to_png, ()),
                                       (set_saturation, (0,)),
                                       (dye, (r, g, b))),
                          results_dir, naming_fn=lambda name: colored_name(name, colname))
        # execute_for_batch(images_dir, ((convert_to_png, ()), (dye, (r, g, b)), (copypaste_image, ('puff_slash.png', 0, 0, 64, 64, 0, 0))), results_dir, naming_fn=lambda name: colored_name(name, colname))
        # execute_for_batch(images_dir, (), results_dir, naming_fn=lambda name: colored_name(name, colname))


if __name__ == "__main__":
    main()
