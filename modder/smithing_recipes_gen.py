import json
import os
from constants import *


class SmithingType:
    def __init__(self, process, base_prefixes, result_prefixes, addition_forge, addition_fabric, template):
        self.process = process
        self.base_prefixes = base_prefixes
        self.result_prefixes = result_prefixes
        self.addition_forge = addition_forge
        self.addition_fabric = addition_fabric
        self.template = template


gilded_prefixes = ["gilded_", "ceremonial", "ceremonial_"]

smithing_types = [
    SmithingType("gilding", [""], gilded_prefixes, {"tag": "forge:ingots/gold"}, {"tag": "c:gold_ingots"}, "magistuarmory:gilding_template"),
    SmithingType("darkening", [""], ["dark_"], {"item": "minecraft:black_dye"}, {"item": "minecraft:black_dye"}, "magistuarmory:darkening_template"),
    SmithingType("gilding", ["dark_"], ["gilded_dark_", "dark_gilded_"], {"tag": "forge:ingots/gold"}, {"tag": "c:gold_ingots"}, "magistuarmory:gilding_template"),
    SmithingType("darkening", gilded_prefixes, ["gilded_dark_", "dark_gilded_"], {"item": "minecraft:black_dye"}, {"item": "minecraft:black_dye"}, "magistuarmory:darkening_template"),
    SmithingType("silvering", ["dark_"], ["silvered_dark_", "dark_silvered_"], {"tag": "forge:ingots/silver"}, {"tag": "c:silver_ingots"}, "magistuarmory:gilding_template"),
    SmithingType("bronzing", [""], ["bronzed_"], {"tag": "forge:ingots/bronze"}, {"tag": "c:bronze_ingots"}, "magistuarmory:gilding_template"),
    SmithingType("darkening", ["dark_"], ["darkblued_"], {"item": "minecraft:lapis_lazuli"}, {"item": "minecraft:lapis_lazuli"}, "magistuarmory:darkening_template"),
    SmithingType("darkening", ["gilded_dark_", "dark_gilded_"], ["gilded_darkblued_", "darkblued_gilded_"], {"item": "minecraft:lapis_lazuli"}, {"item": "minecraft:lapis_lazuli"}, "magistuarmory:darkening_template"),
    SmithingType("gilding", ["darkblued_"], ["gilded_darkblued_", "darkblued_gilded_"], {"tag": "forge:ingots/gold"},{"tag": "c:gold_ingots"}, "magistuarmory:gilding_template"),
    SmithingType("fully_gilding", ["", "gilded_", "ceremonial", "ceremonial_", "gilded_dark_", "dark_", "darkblued_", "silvered_dark_", "dark_silvered_", "bronzed_", "gilded_darkblued_", "darkblued_gilded_"], ["fully_gilded_"], {"tag": "forge:ingots/gold"},{"tag": "c:gold_ingots"}, "magistuarmory:fully_gilding_template"),
]

smithing_dict = dict()
for smithing_type in smithing_types:
    for result_prefix in smithing_type.result_prefixes:
        if result_prefix not in smithing_dict:
            smithing_dict[result_prefix] = []
        smithing_dict[result_prefix].append(smithing_type)

all_prefixes = sorted({r for t in smithing_types for r in t.result_prefixes}, key=lambda r: len(r), reverse=True)


def generate_smithing_recipes(items, modid):
    for recipe_dir_path in recipe_dir_paths.values():
        if not os.path.exists(recipe_dir_path):
            os.makedirs(recipe_dir_path)
    for item in items:
        if item.split(':')[0] != modid:
            continue
        result_prefix = None
        for r in all_prefixes:
            if item.split(':')[-1].startswith(r):
                result_prefix = r
                break
        if result_prefix is None:
            continue
        for smithing_type in smithing_dict[result_prefix]:
            for base_prefix in smithing_type.base_prefixes:
                base_item = find_base_item(item, base_prefix, result_prefix, items)
                if base_item is not None:
                    save_smithing_recipe(base_item, item, smithing_type, forge)
                    save_smithing_recipe(base_item, item, smithing_type, fabric)


def find_base_item(result_item, base_prefix, result_prefix, items):
    base_id = result_item.split(":")[-1].replace(result_prefix, base_prefix)
    for item in items:
        if item.split(":")[-1] == base_id:
            return item
    return None


def save_smithing_recipe(base_item, result_item, smithing_type, platform):
    with open(f'{recipe_dir_paths[platform]}/{result_item.split(":")[-1]}_from_{base_item.split(":")[-1]}_{smithing_type.process}.json', 'w') as f:
        json.dump(get_smithing_recipe(base_item, result_item, smithing_type, platform), f, indent=4)


def get_smithing_recipe(base_item, result_item, smithing_type, platform):
    recipe = {
        "type": "minecraft:smithing_transform" if not minecraft_version.startswith("1.19") else "minecraft:smithing",
        "base": {
            "item": base_item
        },
        "addition": smithing_type.addition_forge if platform == 'forge' else smithing_type.addition_fabric,
        "result": {
            "item": result_item,
            "count": 1
        }
    }
    if not minecraft_version.startswith("1.19"):
        recipe["template"] = {"item": smithing_type.template}
    return recipe


