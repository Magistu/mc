from paths import *
import re

variants = {
    "orange": ("orange",),
    "magenta": ("magenta",),
    "light_blue": ("light_blue",),
    "yellow": ("yellow",),
    "lime": ("lime",),
    "pink": ("pink",),
    "gray": ("gray",),
    "light_gray": ("light_gray",),
    "cyan": ("cyan",),
    "purple": ("purple",),
    "blue": ("blue",),
    "brown": ("brown",),
    "green": ("green",),
    "red": ("red",),
    "black": ("black",),
    "white": ("white",),
}

filename = "{0}_puff_and_slash_leggings.json"

contents = """{
    "type": "minecraft:crafting_shaped",
    "pattern": [
        "aaa",
        "a a",
        "ada"
    ],
    "key": {
        "a": {
            "tag": "magistuarmory:woolen_fabrics"
        },
        "d": {
            "item": "minecraft:{0}_dye"
        }
    },
    "result": {
        "item": "magistuarmoryaddon:{0}_puff_and_slash_leggings",
        "count": 1
    }
}"""


def main():
    text = re.sub(r"(?<![0-9{}])}", "}}", re.sub(r"\{(?![0-9{}])", "{{", contents))
    print(text)
    for name, values in variants.items():
        with open(results_dir + "/" + filename.format(name), "w") as f:
            f.write(text.format(*values))


if __name__ == "__main__":
    main()
