import itertools

from constants import *
from code_helper import to_camel_case


class ArmorPiece:
    def __init__(self, slot, armor_type, id, clazz, durability, defense, color):
        self.slot = slot
        self.armor_type = armor_type
        self.id = id
        self.clazz = clazz
        self.durability = durability
        self.defense = defense
        self.color = color


class ArmorSet:
    
    def __init__(self, type_name, modid, id, model_id, helmet_id, chestplate_id, leggings_id, boots_id, helmet_class, chestplate_class, leggings_class, boots_class, toughness, knockback_resistance, boots_durability, leggings_durability, chest_durability, helmet_durability, boots_defense, leggings_defense, chest_defense, helmet_defense, enchantment_value, sound, repair_material, model_class_name, helmet_color, chest_color, leggings_color, boots_color):
        self.helmet = ArmorPiece(head, "helmet", helmet_id, helmet_class, helmet_durability, helmet_defense, helmet_color)
        self.chestplate = ArmorPiece(head, "chestplate", chestplate_id, chestplate_class, chest_durability, chest_defense, chest_color)
        self.leggings = ArmorPiece(head, "leggings", leggings_id, leggings_class, leggings_durability, leggings_defense, leggings_color)
        self.boots = ArmorPiece(head, "boots", boots_id, boots_class, boots_durability, boots_defense, boots_color)

        self.type_name = type_name
        self.modid = modid
        self.id = id
        self.model_id = model_id
        self.slots = {p.slot: p for p in (self.helmet, self.chestplate, self.leggings, self.boots) if p.clazz != ""}
        self.toughness = toughness
        self.knockback_resistance = knockback_resistance
        self.enchantment_value = enchantment_value
        self.sound = sound
        self.repair_material = repair_material
        self.model_class_name = model_class_name
        self.config_class_name = to_camel_case(self.type_name.lower()) + 'Config'
        self.config_field_name = to_camel_case(self.type_name.lower())
    
    @classmethod
    def of(cls, row):
        i = itertools.count()
        return cls(row[next(i)], row[next(i)], row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  float(row[next(i)]),  float(row[next(i)]),  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)],  int(row[next(i)]),  row[next(i)],  row[next(i)], row[next(i)],  row[next(i)],  row[next(i)],  row[next(i)], row[next(i)])

    @property
    def ids(self):
        return [p.id for p in self.slots.values()]

    def armor_type_code(self, configured=True):
        return f'public static final ArmorType {self.type_name.upper()} = new ArmorType(new ResourceLocation(\"{self.modid}\", \"{self.id}\"), new ResourceLocation(\"{self.model_id}\"), {self.toughness}f, {self.knockback_resistance}f, new Integer[] {{ {self.boots.durability}, {self.leggings.durability}, {self.chestplate.durability}, {self.helmet.durability} }}, new Integer[] {{ {self.boots.defense}, {self.leggings.defense}, {self.chestplate.defense}, {self.helmet.defense} }}, {self.enchantment_value}, {self.sound}, {"ARMOR_CONFIG." + self.config_field_name if configured else "true"}, {self.repair_material});\n'

    def register_armor_code(self):
        return '\t'.join(f'public static final @Nullable RegistrySupplier<MedievalArmorItem> {p.id.upper()} = INSTANCE.add{p.clazz}(\"{p.id.lower()}\", {armor_types_class}.{self.type_name.upper()}, ArmorItem.Type.{slot.upper()}, new Item.Properties(){".tab(ModCreativeTabs.ARMOR)" if minecraft_version.startswith("1.19") else ""}{f", {p.color}" if p.color else ""});\n' for slot, p in self.slots.items())

    def config_declaration_code(self):
        return f'''@ConfigEntry.Gui.CollapsibleObject
    public {self.config_class_name} {self.config_field_name};'''

    def armor_config_code(self):
        code = f'''public static class {self.config_class_name}
    {{
        @ConfigEntry.Gui.RequiresRestart
        public boolean enabled;
        @ConfigEntry.Gui.RequiresRestart
        public float toughness;'''
        code_2 = f'''
        
        public {self.config_class_name}() {{
            this.enabled = true;
            this.toughness = {self.toughness:.2f}f;'''
        for piece in self.slots.values():
            code += f'''
        @ConfigEntry.Gui.RequiresRestart
        public int {piece.armor_type}Durability;
        @ConfigEntry.Gui.RequiresRestart
        public int {piece.armor_type}Defense;'''
            code_2 += f'''
            this.{piece.armor_type}Durability = {piece.durability};
			this.{piece.armor_type}Defense = {piece.defense};'''
        code += code_2
        code += '''
        }}
    }}'''
        return code
    
    def config_assignment_code(self):
        return f'this.{self.config_field_name} = new {self.config_class_name}();'
    
    def armor_layer_code(self):
        return f'public static final ModelLayerLocation {self.model_id.split(":")[-1].upper()}_LOCATION = INSTANCE.addArmorModel("{self.model_id.split(":")[-1].lower()}", {self.model_class_name}::createLayer);'

def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))
