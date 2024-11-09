project_id_field = 'EpicKnightsAddon.ID'
armor_dict = {
	'silvered_dark_maximilian_helmet': ['silvered_dark_maximilian_helmet'],
	'silvered_dark_bellows_maximilian_helmet': ['silvered_dark_bellows_maximilian_helmet'],
	'gilded_grand_bascinet': ['gilded_grand_bascinet'],
	'gilded_steel_puff_and_slash': ['gilded_steel_puff_and_slash_chestplate', 'gilded_steel_puff_and_slash_boots'],
	'ceremonial_kastenbrust': ['ceremonial_kastenbrust_chestplate', 'ceremonial_kastenbrust_boots'],
	'heavy_cuirassier': ['heavy_cuirassier_chestplate', 'heavy_cuirassier_boots'],
	'dark_heavy_cuirassier': ['dark_heavy_cuirassier_chestplate', 'dark_heavy_cuirassier_boots'],
	'silvered_dark_maximilian': ['silvered_dark_maximilian'],
	'gilded_xiv_century_knight': ['gilded_xiv_century_knight_chestplate', 'gilded_xiv_century_knight_boots'],
	'mail_haubergeon': ['mail_haubergeon_chestplate', 'mail_haubergeon_leggings', 'mail_haubergeon_boots'],
	'english_knight': ['english_knight_chestplate', 'english_knight_boots'],
	'gilded_half_armor': ['gilded_half_armor'],
	'gilded_maximilian': ['gilded_maximilian_chestplate', 'gilded_maximilian_leggings', 'gilded_maximilian_boots'],
	'coat_of_plates': ['coat_of_plates_chestplate', 'coat_of_plates_boots'],
	'silvered_dark_half_armor': ['silvered_dark_half_armor'],
	'gilded_dark_gothic': ['gilded_dark_gothic', 'gilded_dark_gothic_leggings', 'gilded_dark_gothic_boots'],
	'gilded_gothic': ['gilded_gothic', 'gilded_gothic_leggings', 'gilded_gothic_boots'],
	'exquisite_ceremonial_armet': ['exquisite_ceremonial_armet'],
	'gilded_greenwich': ['gilded_greenwich_chestplate', 'gilded_greenwich_leggings', 'gilded_greenwich_boots'],
	'greenwich': ['greenwich_chestplate', 'greenwich_leggings', 'greenwich_boots']
}


def main():
	armor_types_code = ''
	armor_items_code = ''
	for armor_type, armor_items in armor_dict.items():
		armor_types_code += f'public static final ArmorType {armor_type.upper()} = new ArmorType(new ResourceLocation({project_id_field}, \"{armor_type}\"), new ResourceLocation(\"default\"), 1.25f, 0.0f, new Integer[] {{ 210, 300, 320, 250 }}, new Integer[] {{ 2, 5, 7, 3 }}, 9, SoundEvents.ARMOR_EQUIP_IRON, true, Platform.isForge() ? "forge:ingots/steel" : "c:steel_ingots");\n'
		for armor_item in armor_items:
			armor_items_code += f'public static final @Nullable RegistrySupplier<MedievalArmorItem> {armor_item.upper()} = INSTANCE.addMedievalArmorItem(\"{armor_item}\", AddonArmorTypes.{armor_type.upper()}, ArmorItem.Type.{get_type(armor_item)}, new Item.Properties());\n'
		armor_types_code += '\n'
		armor_items_code += '\n'
	print(armor_types_code)
	print(armor_items_code)
	

def get_type(armor_item):
	if 'chestplate' in armor_item:
		return 'CHESTPLATE'
	if 'leggings' in armor_item:
		return 'LEGGINGS'
	if 'boots' in armor_item:
		return 'BOOTS'
	return 'HELMET'


if __name__ == '__main__':
	main()
