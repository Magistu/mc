minecraft_version = "1.20.2"


# modid = "slavicarmory"
# main_package = f"magistuarmory.{modid}"
# main_class = "EpicKnightsSlavicArmory"
# en_us_source_path = f"/home/lut/Java/modding/Epic-Knights-Expansion-To-The-East-{minecraft_version}-crossversion/common/src/main/resources/assets/{modid}/lang/en_us.json"

modid = "magistuarmoryaddon"
main_package = f"magistuarmory.addon"
main_class = "EpicKnightsAddon"
en_us_source_path = f"/home/lut/Java/modding/Epic-Knights-Addon-{minecraft_version}-crossversion/common/src/main/resources/assets/{modid}/lang/en_us.json"

# modid = "antiquelegacy"
# main_package = f"magistuarmory.{modid}"
# main_class = "EpicKnightsAntiqueLegacy"
# en_us_source_path = f"/home/lut/Java/modding/Epic-Knights-Antique-Legacy-{minecraft_version}-crossversion/common/src/main/resources/assets/{modid}/lang/en_us.json"

# modid = "magistuarmory"
# main_package = modid"
# main_class = "EpicKnights"
# en_us_source_path = f"/home/lut/Java/modding/Epic-Knights-{minecraft_version}-crossversion/common/src/main/resources/assets/{modid}/lang/en_us.json"

items_class = "AddonItems"
armor_types_class = "AddonArmorTypes"
weapon_types_class = "AddonWeaponTypes"
layers_class = "AddonModels"

# items_class = "ModItems"
# armor_types_class = "ArmorTypes"
# weapon_types_class = "WeaponTypes"
# layers_class = "ModModels"
# en_us_source_path = f"/home/lut/Java/modding/Epic-Knights-{minecraft_version}-crossversion/common/src/main/resources/assets/{modid}/lang/en_us.json"

# head = "HEAD"
# body = "BODY"
# legs = "LEGS"
# feet = "FEET"
head = "HELMET"
body = "CHESTPLATE"
legs = "LEGGINGS"
feet = "BOOTS"

fabric = "fabric"
forge = "forge"
neoforge = "neoforge"

main_path = main_package.replace(".", "/")
weapons_xls_path = "/home/lut/Java/modding/weapons.xls"
armor_xls_path = "/home/lut/Java/modding/armor.xls"
decorations_xls_path = "/home/lut/Java/modding/decorations.xls"
lang_dir = f"new_files/common/src/main/resources/assets/{modid}/lang"
en_us_path = f"{lang_dir}/en_us.json"
item_models_dir = f"new_files/common/src/main/resources/assets/{modid}/models/item"
item_dir = f"new_files/common/src/main/java/com/{main_path}/item"
weapon_types_path = f"{item_dir}/{weapon_types_class}.java"
armor_dir = f"{item_dir}/armor"
armor_types_path = f"{armor_dir}/{armor_types_class}.java"
items_path = f"{item_dir}/{items_class}.java"
config_dir = f"new_files/common/src/main/java/com/{main_path}/config"
weapons_config_path = f"{config_dir}/WeaponsConfig.java"
armor_config_path = f"{config_dir}/ArmorConfig.java"
blasting_recipes_dir = f"new_files/common/src/main/resources/data/{modid}/recipes/furnace"
blasting_recipes_path = f"{blasting_recipes_dir}/blastin_recipes.json"
weapon_models_path = "weapon_models.json"
all_materials = ["wood", "stone", "iron", "diamond", "gold", "netherite", "copper", "silver", "steel", "tin", "bronze"]
predicates = ["", "blocking", "raised"]
model_dir = f"new_files/common/src/main/java/com/{main_path}/client/render/model"
layers_path = f"{model_dir}/{layers_class}"
if minecraft_version.startswith("1.21"):
    fabric_recipe_dir_path = f"new_files/common/src/main/resources/data/{modid}/recipes"
    forge_recipe_dir_path = f"new_files/common/src/main/resources/data/{modid}/recipes"
else:
    fabric_recipe_dir_path = f"new_files/fabric/src/main/resources/data/{modid}/recipes"
    forge_recipe_dir_path = f"new_files/forge/src/main/resources/data/{modid}/recipes"
neoforge_recipe_dir_path = f"new_files/common/src/main/resources/data/{modid}/recipes"
recipe_dir_paths = {
    fabric: fabric_recipe_dir_path,
    forge: forge_recipe_dir_path,
    neoforge: neoforge_recipe_dir_path
}


