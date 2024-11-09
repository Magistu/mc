from constants import *

class Decoration:
    def __init__(self, id, modid, class_name, slot, model_class, armor_type, color):
        self.id = id
        self.modid = modid
        self.class_name = class_name
        self.slot = slot
        self.model_class = model_class
        self.armor_type = armor_type
        self.color = color
        self.decor_id = f"{id}_decoration"

    @classmethod
    def of(cls, row):
        return cls(row[0], row[1], row[2],  row[3],  row[4],  row[5],  row[6])
    
    def register_decoration_code(self):
        if self.armor_type != '':
            if self.color != '':
                return f'public static final RegistrySupplier<{self.class_name}> {self.id.upper()}_DECORATION = INSTANCE.addDyeableWearableArmorDecorationItem("{self.id.lower()}_decoration", {self.armor_type}, ArmorItem.Type.{self.slot}, new Item.Properties(){".tab(ModCreativeTabs.ARMOR_DECORATIONS)" if minecraft_version.startswith("1.19") else ""}, {self.color});'
            else:
                return f'public static final RegistrySupplier<{self.class_name}> {self.id.upper()}_DECORATION = INSTANCE.addWearableArmorDecorationItem("{self.id.lower()}_decoration", {self.armor_type}, ArmorItem.Type.{self.slot}, new Item.Properties(){".tab(ModCreativeTabs.ARMOR_DECORATIONS)" if minecraft_version.startswith("1.19") else ""});'
        else:
            if self.color != '':
                return f'public static final RegistrySupplier<{self.class_name}> {self.id.upper()}_DECORATION = INSTANCE.addDyeableArmorDecorationItem("{self.id.lower()}_decoration", () -> new {self.class_name}(new ResourceLocation({main_class}.ID, "{self.id.lower()}"), new Item.Properties(){".tab(ModCreativeTabs.ARMOR_DECORATIONS)" if minecraft_version.startswith("1.19") else ""}, ArmorItem.Type.{self.slot}, {self.color}));'
            else:
                return f'public static final RegistrySupplier<{self.class_name}> {self.id.upper()}_DECORATION = INSTANCE.addArmorDecorationItem("{self.id.lower()}_decoration", () -> new {self.class_name}(new ResourceLocation({main_class}.ID, "{self.id.lower()}"), new Item.Properties(){".tab(ModCreativeTabs.ARMOR_DECORATIONS)" if minecraft_version.startswith("1.19") else ""}, ArmorItem.Type.{self.slot}));'
    
    def decoration_layer_code(self, model_field=''):
        return f'public static final ModelLayerLocation {self.id.upper()}_LOCATION = INSTANCE.addDecorationModel("{self.id.lower()}", {f"{self.model_class}::createLayer" if model_field == "" else "() -> " + model_field});'
