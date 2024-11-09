import itertools
from collections import Counter

from armor_set import ArmorSet
from code_helper import *
from constants import *
from decoration import Decoration
from smithing_recipes_gen import generate_smithing_recipes
from weapon import Weapon
import json
import warnings
import xlrd
import os
warnings.filterwarnings('ignore', 'The iteration is not making good progress')


mod_ids = [modid]


def merge_dicts(a, b):
    return {key: value for (key, value) in itertools.chain(a.items(), b.items())}

def generate_armor_types(armor, configured=True):
    if not os.path.exists(armor_dir):
        os.makedirs(armor_dir)
    code = f"""package com.{main_package}.item.armor;

import com.{main_package}.{main_class};
import com.{main_package}.config.ArmorConfig;
import com.magistuarmory.item.armor.ArmorType;
import dev.architectury.platform.Platform;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.tags.TagKey;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.crafting.Ingredient;

public class {armor_types_class}
{{
"""
    if configured:
        code += f"""\tpublic static final ArmorConfig ARMOR_CONFIG = {main_class}.CONFIG.armor;
    
"""
    for armor_set in armor:
        code += f"\t{armor_set.armor_type_code(configured)}\n"
    code += "}\n"
    with open(armor_types_path, "w") as fout:
        fout.write(code)

def generate_weapon_types(weapons, configured=True):
    if not os.path.exists(item_dir):
        os.makedirs(item_dir)
    code = f"""package com.{main_package}.item;

import com.{main_package}.{main_class};
import com.{main_package}.config.WeaponsConfig;
import com.magistuarmory.item.WeaponType;

public class {weapon_types_class}
{{
"""
    if configured:
        code += f"""\tpublic static final WeaponsConfig WEAPONS_CONFIG = {main_class}.CONFIG.weapons;
	
"""
    for weapon in weapons:
        code += f"\t{weapon.weapon_type_code(configured)}\n"
    code += "}\n"
    with open(weapon_types_path, "w") as fout:
        fout.write(code)


def generate_en_us_translation(items):
    if not os.path.exists(lang_dir):
        os.makedirs(lang_dir)
    
    dic = {f'item.{modid}.{item}': item for item in items}
    
    with open(en_us_source_path, 'r', encoding='utf-8-sig') as fin, open(en_us_path, 'w') as fout:
        en_us = json.loads(fin.read())
        data = {}
        for key, item in dic.items():
            data[key] = en_us[key] if key in en_us else "??" + to_capitalized_text(item)
        json.dump(data, fout, indent=4)

def generate_register_items_code(weapons, armor, decorations):
    if not os.path.exists(item_dir):
        os.makedirs(item_dir)
    code = f"""package com.{main_package}.item;

import com.{main_package}.{main_class};
import com.{main_package}.item.armor.{armor_types_class};
import com.magistuarmory.api.item.ModItemsProvider;
import com.magistuarmory.item.*;
import com.magistuarmory.item.armor.DyeableWearableArmorDecorationItem;
import com.magistuarmory.item.armor.MedievalArmorItem;
import com.magistuarmory.item.armor.MedievalHorseArmorItem;
import dev.architectury.registry.registries.RegistrySupplier;
import me.shedaniel.cloth.clothconfig.shadowed.blue.endless.jankson.annotation.Nullable;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.ArmorItem;
import net.minecraft.world.item.DyeColor;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.SmithingTemplateItem;
import net.minecraft.world.level.material.MapColor;

import java.util.List;

public class {items_class} extends ModItemsProvider
{{
	public static AddonItems INSTANCE = new AddonItems();
	
	//Weapons
"""
    for weapon in weapons:
        code += f"\t{weapon.register_weapon_code()}\n"
    code += "\n\n\t//Armor\n"
    for armor_set in armor:
        code += f"\t{armor_set.register_armor_code()}\n"
    code += "\n\n\t//Decoration\n"
    for decoration in decorations:
        code += f"\t{decoration.register_decoration_code()}\n"
    code += f"""
    public AddonItems()
	{{
		super({main_class}.ID);
	}}
}}
"""
    with open(items_path, "w") as fout:
        fout.write(code)

def generate_armor_config(armor):
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    code = f"""package com.{main_package}.config;

import me.shedaniel.autoconfig.annotation.ConfigEntry;
import me.shedaniel.autoconfig.annotation.Config;
import me.shedaniel.autoconfig.ConfigData;

@Config(name = "armors")
public class ArmorConfig implements ConfigData
{{
"""
    for armor_set in armor:
        code += f"\t{armor_set.config_declaration_code()}\n"
    code += """
    public ArmorConfig() {
"""
    for armor_set in armor:
        code += f"\t\t{armor_set.config_assignment_code()}\n"
    code += "\t}\n\n"
    # for armor_set in armor:
    #     code += f"\t{armor.armor_config_code()}\n"
    code += "}\n"
    with open(armor_config_path, "w") as fout:
        fout.write(code)

def generate_weapon_config(weapons):
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    code = f"""package com.{main_package}.config;

import me.shedaniel.autoconfig.annotation.ConfigEntry;
import me.shedaniel.autoconfig.annotation.Config;
import me.shedaniel.autoconfig.ConfigData;

@Config(name = "weapons")
public class WeaponsConfig implements ConfigData
{{
"""
    for weapon in weapons:
        code += f"\t{weapon.config_declaration_code()}\n"
    code += """
    public WeaponsConfig() {
"""
    for weapon in weapons:
        code += f"\t\t{weapon.config_assignment_code()}\n"
    code += "\t}\n\n"
    for weapon in weapons:
        code += f"\t{weapon.weapon_config_code()}\n"
    code += "}\n"
    with open(weapons_config_path, "w") as fout:
        fout.write(code)

def generate_layers(armor, decorations):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    code = f"""package com.{main_package}.client.render.model;

import com.{main_package}.{main_class};
import com.{main_package}.client.render.model.armor.*;
import com.{main_package}.client.render.model.decoration.*;
import com.magistuarmory.api.client.render.model.ModModelsProvider;
import com.magistuarmory.client.render.model.decoration.RondelModel;
import com.magistuarmory.client.render.model.decoration.TopDecorationModel;
import net.minecraft.client.model.geom.ModelLayerLocation;
import net.minecraft.client.model.geom.builders.LayerDefinition;

public class {layers_class} extends ModModelsProvider
{{
	public static {layers_class} INSTANCE = new {layers_class}({main_class}.ID);

    // Armor
"""
    for armor_set in distinct((a for a in armor if a.model_id.split(":")[0] == modid), key=lambda a: a.model_id):
        code += f"\t{armor_set.armor_layer_code()}\n"
    code += "\n\t// Decorations\n"
    counts = Counter(d.model_class for d in decorations)
    preassigned_model_classes = [m for m, n in counts.items() if n > 1]
    for model in preassigned_model_classes:
        code += f"\tpublic static final LayerDefinition {to_snake_case(model).upper()} = {model}.createLayer();\n"
    code += "\n\n"
    for decoration in decorations:
        model = to_snake_case(decoration.model_class).upper() if decoration.model_class in preassigned_model_classes else ""
        code += f"\t{decoration.decoration_layer_code(model)}\n"
    code += f"""
    public {layers_class}(String modId)
    {{
        super(modId);
    }}
}}"""
    with open(layers_path, "w") as fout:
        fout.write(code)

def generate_armor_models(armor):
    if not os.path.exists(item_models_dir):
        os.makedirs(item_models_dir)
    for armor_set in armor:
        for piece in armor_set.slots.values():
            has_overlay = piece.clazz.find("Dyeable") >= 0
            data = {
                "parent": "item/generated",
                "textures": {
                }
            }
            data["textures"]["layer0"] = f"{armor_set.modid}:item/{piece.id}"
            if has_overlay:
                data["textures"]["layer1"] = f"{armor_set.modid}:item/{piece.id}_overlay"
            with open(f"{item_models_dir}/{piece.id}.json", "w") as fout:
                json.dump(data, fout, indent=4)

def generate_decoration_models(decorations):
    if not os.path.exists(item_models_dir):
        os.makedirs(item_models_dir)
    for decoration in decorations:
        data = {
            "parent": "item/generated",
            "textures": {
            }
        }
        has_overlay = decoration.class_name.find("Dyeable") >= 0
        id = f"{decoration.id}_decoration"
        data["textures"]["layer0"] = f"{decoration.modid}:item/{id}"
        if has_overlay:
            data["textures"]["layer1"] = f"{decoration.modid}:item/{id}_overlay"
        with open(f"{item_models_dir}/{id}.json", "w") as fout:
            json.dump(data, fout, indent=4)

def generate_weapon_models(weapons):
    if not os.path.exists(item_models_dir):
        os.makedirs(item_models_dir)
    with open(weapon_models_path, "r") as fin:
        presets = json.load(fin)
        for weapon in weapons:
            one_material = len(weapon.materials) == 1
            base_id = weapon.ids[0] if one_material else weapon.id
            if weapon.type not in presets:
                raise ValueError(f"weapon type \"{weapon.type}\" is unknown")
            data = {
                "parent": "item/handheld"
            }
            if one_material:
                data["textures"] = {
                    "layer0": f"{weapon.modid}:item/{weapon.ids[0]}"
                }
            blocking_type = weapon.type + "_blocking"
            if blocking_type in presets:
                data["overrides"] = [{"predicate": {"blocking": 1}, "model": f"{weapon.modid}:item/{base_id}_blocking"}]
                with open(f"{item_models_dir}/{base_id}_blocking.json",
                          "w") as fout:
                    json.dump(merge_dicts(data, presets[blocking_type]), fout, indent=4)
                if not one_material:
                    generate_weapon_model_inheritors(weapon, predicate="blocking", predicate_value=0)
                    generate_weapon_model_inheritors(weapon, predicate="blocking", predicate_value=1)
            raised_type = weapon.type + "_raised"
            if raised_type in presets:
                data["overrides"] = [
                    {"predicate": {"magistuarmory:raised": 1}, "model": f"{weapon.modid}:item/{weapon.id}_raised"}]
                with open(f"{item_models_dir}/{base_id}_raised.json", "w") as fout:
                    json.dump(merge_dicts(data, presets[raised_type]), fout, indent=4)
                if not one_material:
                    generate_weapon_model_inheritors(weapon, predicate="raised", predicate_value=0)
                    generate_weapon_model_inheritors(weapon, predicate="raised", predicate_value=1)
            with open(f"{item_models_dir}/{base_id}.json", "w") as fout:
                json.dump(merge_dicts(data, presets[weapon.type]), fout, indent=4)

def generate_weapon_model_inheritors(weapon, predicate="", predicate_value=0):
    if predicate not in predicates:
        raise ValueError(f"weapon predicate \"{predicate}\" is unknown, known are: {predicates}")
    predicate_id = "magistuarmory:raised" if predicate == "raised" else predicate
    parent_id = f"{weapon.id}_{predicate}" if predicate else weapon.id
    for id in weapon.ids:
        if predicate_value:
            id = f"{id}_{predicate}"
        data = {
            "parent": f"{weapon.modid}:item/{parent_id}"
        }
        if not predicate_value:
            data["overrides"] = [
                {
                    "predicate": {
                        predicate_id: 1
                    },
                    "model": f"magistuarmory:item/{id}_{predicate}"
                }
            ]
        with open(f"{item_models_dir}/{id}.json", "w") as fout:
            json.dump(data, fout, indent=4)

def generate_blasting_recipes(weapons, armor):
    if not os.path.exists(blasting_recipes_dir):
        os.makedirs(blasting_recipes_dir)
    data = {
        "iron": {
            "type": "minecraft:blasting",
            "ingredient": [],
            "result": "minecraft:iron_nugget",
            "experience": 0.1,
            "cookingtime": 100
        },
        "gold": {
            "type": "minecraft:blasting",
            "ingredient": [],
            "result": "minecraft:gold_nugget",
            "experience": 0.1,
            "cookingtime": 100
        },
        "steel": {
            "type": "minecraft:blasting",
            "ingredient": [],
            "result": "magistuarmory:steel_nugget",
            "experience": 0.1,
            "cookingtime": 100
        }
    }
    for weapon in weapons:
        for material in [m for m in weapon.materials if m in data.keys()]:
            data[material]["ingredient"].append({"item": f"{weapon.modid}:{weapon.id_of(material)}"})
    for armor_set in armor:
        material = ""
        if "iron" in armor_set.repair_material:
            material = "iron"
        elif "gold" in armor_set.repair_material:
            material = "gold"
        elif "steel" in armor_set.repair_material:
            material = "steel"
        if not material:
            continue
        for id in armor_set.ids:
            data[material]["ingredient"].append({"item": f"{armor_set.modid}:{id}"})
    for key, val in data.items():
        with open(f"{blasting_recipes_dir}/{key}_nugget_blasting.json", "w") as fout:
            json.dump(val, fout, indent=4)


def get_items(weapons, armor, decorations):
    return sum([w.ids for w in weapons], []) + sum([w.ids for w in armor], []) + [d.decor_id for d in decorations]


def generate():
    rb = xlrd.open_workbook(weapons_xls_path, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    weapons = []
    resource_locations = []
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        if not row[0]:
            continue
        weapon = Weapon.of(row)
        resource_locations += (f'{weapon.modid}:{id}' for id in weapon.ids)
        if weapon.modid not in mod_ids:
            continue
        weapons.append(weapon)
    weapons.sort(key=lambda w: (w.type, w.type_name))
    generate_weapon_types(weapons)
    generate_weapon_config(weapons)
    generate_weapon_models(weapons)
    rb = xlrd.open_workbook(armor_xls_path, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    armor = []
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        if not row[0]:
            continue
        armor_set = ArmorSet.of(row)
        resource_locations += (f'{armor_set.modid}:{id}' for id in armor_set.ids)
        if armor_set.modid not in mod_ids:
            continue
        armor.append(armor_set)
    rb = xlrd.open_workbook(decorations_xls_path, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    decorations = []
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        if not row[0]:
            continue
        decoration = Decoration.of(row)
        resource_locations.append(f'{decoration.modid}:{decoration.decor_id}')
        if decoration.modid not in mod_ids:
            continue
        decorations.append(decoration)

    items = get_items(weapons, armor, decorations)
    generate_armor_types(armor)
    generate_armor_config(armor)
    generate_armor_models(armor)
    generate_decoration_models(decorations)
    generate_layers(armor, decorations)
    generate_blasting_recipes(weapons, armor)
    generate_register_items_code(weapons, armor, decorations)
    generate_en_us_translation(items)
    generate_smithing_recipes(resource_locations, modid)


if __name__ == '__main__':
    generate()
