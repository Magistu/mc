from utils import *
from paths import *
import shutil

tag_replaces = {
    "forge:gems/diamond": "c:diamonds",
    "forge:cobblestone": "c:cobblestones",
    "forge:rods/wooden": "c:wooden_rods",

    "forge:ingots/gold": "c:gold_ingots",
    "forge:nuggets/gold": "c:gold_nuggets",
    "forge:ingots/iron": "c:iron_ingots",
    "forge:nuggets/iron": "c:iron_nuggets",
    "forge:ingots/netherite": "c:netherite_ingots",
    "forge:nuggets/netherite": "c:netherite_nuggets",

    "forge:ingots/tin": "c:tin_ingots",
    "forge:nuggets/tin": "c:tin_nuggets",
    "forge:ingots/copper": "c:copper_ingots",
    "forge:nuggets/copper": "c:copper_nuggets",
    "forge:ingots/silver": "c:silver_ingots",
    "forge:nuggets/silver": "c:silver_nuggets",
    "forge:ingots/bronze": "c:bronze_ingots",
    "forge:nuggets/bronze": "c:bronze_nuggets",
    "forge:plates/steel": "c:steel_plates",
    "forge:ingots/steel": "c:steel_ingots",
    "forge:nuggets/steel": "c:steel_nuggets",
    "forge:flowers": "c:flowers",
    '"tag": "forge:feathers"': '"item": "minecraft:feather"'
}

tag_materials_replaces = {
    '      "item": "magistuarmory:small_steel_plate"': '      "tag": "magistuarmory:small_plates/steel"',
    '      "item": "magistuarmory:lamellar_rows"': '      "tag": "magistuarmory:lamellar_rows/steel"',
    '      "item": "magistuarmory:steel_chainmail"': '      "tag": "magistuarmory:chainmails/steel"',
    '      "item": "magistuarmory:steel_chain"': '      "tag": "magistuarmory:chains/steel"',
    '      "item": "magistuarmory:steel_ring"': '      "tag": "magistuarmory:rings/steel"',
    '      "item": "magistuarmory:hilt"': '      "tag": "magistuarmory:hilts"',
    '      "item": "magistuarmory:pole"': '      "tag": "magistuarmory:poles"',
    '      "item": "magistuarmory:leather_strip"': '      "tag": "magistuarmory:leather_strips"',
    '      "item": "magistuarmory:woolen_fabric"': '      "tag": "magistuarmory:woolen_fabrics"',
    '      "item": "minecraft:woolen_fabric"': '      "tag": "magistuarmory:woolen_fabrics"',
    '      "item": "minecraft:diamond"': '      "tag": "forge:gems/diamond"',
    '      "item": "minecraft:cobblestone"': '      "tag": "forge:cobblestone"',
    '      "item": "minecraft:stick"': '      "tag": "forge:rods/wooden"',
    '      "item": "minecraft:gold_ingot"': '      "tag": "forge:ingots/gold"',
    '      "item": "minecraft:gold_nugget"': '      "tag": "forge:nuggets/gold"',
    '      "item": "minecraft:iron_ingot"': '      "tag": "forge:ingots/iron"',
    '      "item": "minecraft:iron_nugget"': '      "tag": "forge:nuggets/iron"',
    '      "item": "minecraft:netherite_ingot"': '      "tag": "forge:ingots/netherite"',
    '      "item": "minecraft:netherite_nugget"': '      "tag": "forge:nuggets/netherite"',
    '      "item": "magistuarmory:steel_plate"': '      "tag": "forge:plates/steel"',
    '      "item": "magistuarmory:steel_ingot"': '      "tag": "forge:ingots/steel"',
    '      "item": "magistuarmory:steel_nugget"': '      "tag": "forge:nuggets/steel"'
}


def execute_for_all(files_dir, tasks, results_dir):
    if files_dir != results_dir:
        for filename in os.listdir(files_dir):
            source = files_dir + '/' + filename
            if os.path.isfile(source):
                shutil.copy(source, results_dir + '/' + filename)
    filenames = os.listdir(results_dir)
    for filename in filenames:
        for task, args in tasks:
            task(results_dir + '/' + filename, *args)
        print(filename)


def main():
    for material in ("dragon", "dragonsteel_fire", "myrmex_desert_venom", "dragon_fire", "dragonsteel_ice", "myrmex_jungle", "dragon_ice", "dragonsteel_lightning", "myrmex_jungle_venom", "dragon_lightning", "myrmex_desert"):
        name_replaces = {"bronze": material}
        data_replaces = {"bronze": material, '"0": "magistuarmory:': '"0": "epic_knights_ice_and_fire:', '"particle": "magistuarmory:': '"particle": "epic_knights_ice_and_fire:'}
        tasks = ((replace_data, [data_replaces]), (replace_name, [name_replaces]),)
        execute_for_all(files_dir, tasks, results_dir)


if __name__ == '__main__':
    main()
