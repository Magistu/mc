from re import *

from code_helper import to_camel_case, to_pascal_case
from constants import *


class Weapon:
    def __init__(self, type_name, mod_id, id, materials, has_material_prefix, type, basic_damage, basic_speed, bonus_reach, size_factor, weight, piercing, two_handed, max_block_damage, dismounts, horseback_bonus, flamebladed):
        self.type_name = type_name
        self.modid = mod_id
        self.id = id
        self.materials = all_materials if materials == "all" else split(r' *, *', materials)
        self.has_material_prefix = has_material_prefix
        if not self.has_material_prefix and len(self.materials) > 1:
            raise ValueError(f"you must use material prefix for the weapon {self.modid}:{self.id} made of different materials")
        self.type = type
        self.basic_damage = basic_damage
        self.basic_speed = basic_speed
        self.bonus_reach = bonus_reach
        self.size_factor = size_factor
        self.weight = weight
        self.piercing = piercing
        self.two_handed = two_handed
        self.max_block_damage = max_block_damage
        self.dismounts = dismounts
        self.horseback_bonus = horseback_bonus
        self.flamebladed = flamebladed
        self.config_field_name = to_camel_case(self.type_name.lower())
        self.supply_name = self.type_name.upper() + '_SUPPLY'
        self.weapons_supply_name = to_plural(self.type_name).upper()
        self.config_class_name = to_pascal_case(self.type_name.lower()) + 'Config'
        self.ids = [f"{self.id_of(mat)}" for mat in self.materials]
        self.weapon_types_name = "WeaponTypes" if self.id == "magistuarmory" else "AddonWeaponTypes"
    
    @classmethod
    def of(cls, row):
        return cls(row[0], row[1], row[2], row[3], bool(int(row[4])), row[5], float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), int(row[12]), int(row[13]), float(row[14]), bool(int(row[15])), bool(int(row[16])))

    def id_of(self, material):
        return self.id if not self.has_material_prefix else f"{material}_{self.id}"

    def weapon_type_code(self, configured=True):
        code = ''
        if not configured:
            code += f'public static final WeaponType {self.type_name.upper()} = new WeaponType({self.basic_damage:.2f}f, {self.basic_speed:.2f}f, {self.bonus_reach:.2f}f, {self.size_factor:.2f}f, {self.weight:.2f}f, {int(self.piercing)}, true)'
        else:
            code += f'public static final WeaponType {self.type_name.upper()} = new WeaponType(WEAPONS_CONFIG.{self.config_field_name}.baseAttackDamage, WEAPONS_CONFIG.{self.config_field_name}.baseAttackSpeed, WEAPONS_CONFIG.{self.config_field_name}.bonusAttackReach, {self.size_factor:.2f}f, {self.weight}f, {int(self.piercing)}, WEAPONS_CONFIG.{self.config_field_name}.enabled)'
        if self.two_handed:
            code += f'.setTwoHanded({int(self.two_handed)})'
        if self.flamebladed:
            code += f'.setFlamebladed()'
        if self.max_block_damage:
            code += f'.setMaxBlockDamage({self.max_block_damage:.2f}f)'
        if self.dismounts:
            code += f'.setHalberd()'
        return code + ';'

    def weapon_supply_code(self):
        return f'public static final BiFunction<ModItemTier, Properties, RegistrySupplier<MedievalWeaponItem>> {self.supply_name} = (material, prop) -> INSTANCE.addMedievalWeaponItem(material.getMaterialName() + "_{self.id.lower()}", prop, material, {self.weapon_types_name}.{self.type_name.upper()});'

    def register_supply_code(self):
        return f'public static final WeaponsSupply {self.weapons_supply_name} = INSTANCE.addWeaponsSupply({self.supply_name});'

    def register_weapon_code(self, properties='new Item.Properties()'):
        if self.materials == all_materials:
            return f'{self.weapon_supply_code()}\n\t{self.register_supply_code()}'
        return '\n'.join([f'public static final @Nullable RegistrySupplier<MedievalWeaponItem> {id.upper()} = INSTANCE.addMedievalWeaponItem("{id.lower()}", {properties}{".tab(ModCreativeTabs.PARTICULAR_WEAPONS)" if minecraft_version.startswith("1.19") else ""}, ModItemTier.{mat.upper()}, {self.weapon_types_name}.{self.type_name.upper()});' for id, mat in zip(self.ids, self.materials)])
    
    def weapon_config_code(self):
        return f'''public static class {self.config_class_name}
    {{
        @ConfigEntry.Gui.RequiresRestart
        public boolean enabled;
        @ConfigEntry.Gui.RequiresRestart
        public float baseAttackDamage;
        @ConfigEntry.Gui.RequiresRestart
        public float baseAttackSpeed;
        @ConfigEntry.Gui.RequiresRestart
        public float bonusAttackReach;
        
        public {self.config_class_name}() {{
            this.enabled = true;
            this.baseAttackDamage = {self.basic_damage:.2f}f;
            this.baseAttackSpeed = {self.basic_speed:.2f}f;
            this.bonusAttackReach = {self.bonus_reach:.2f}f;
        }}
    }}'''

    def config_declaration_code(self):
        return f'''@ConfigEntry.Gui.CollapsibleObject
    public {self.config_class_name} {self.config_field_name};'''
    
    def config_assignment_code(self):
        return f'this.{self.config_field_name} = new {self.config_class_name}();'

def to_plural(word):
    if search('[sxz]$', word, IGNORECASE) or search('[^aeioudgkprt]h$', word, IGNORECASE):
        return sub('$', 'es', word, IGNORECASE)
    if search('[aeiou]y$', word, IGNORECASE):
        return sub('y$', 'ies', word, IGNORECASE)
    return word + 's'
