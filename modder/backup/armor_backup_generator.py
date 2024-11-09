import re

from modder.code_helper import to_snake_case

modid = "magistuarmoryaddon"

addon_models_path = 'backup/generated/magistuarmoryaddon/AddonModels.java'
mod_models_path = 'backup/generated/magistuarmoryaddon/ModModels.java'
armor_config_path = 'backup/generated/magistuarmoryaddon/ArmorConfig.java'
armor_types_path = 'backup/generated/magistuarmoryaddon/AddonArmorTypes.java'
items_path = 'backup/generated/magistuarmoryaddon/AddonItems.java'

armor_model_pattern = re.compile(r'INSTANCE\.addArmorModel\("(\w+)", (\w+)::createLayer\);')
armor_type_pattern = re.compile(r'(\w+) = new ArmorType\(new ResourceLocation\("(\w+)", "(\w+)"\), new ResourceLocation\("([\w_:]+)"\), ARMOR_CONFIG\.\w+\.toughness, (\d+\.?\d+)f, new Integer\[] \{[^}]+}, new Integer\[] \{[^}]+}, (\d+), (\w+\.\w+), ARMOR_CONFIG\.\w+\.enabled, (.+)\);')
armor_item_pattern = re.compile(r'INSTANCE\.add(\w+)\("(\w+)", \w+\.(\w+), ArmorItem\.Type\.(\w+), new Item\.Properties\(\)(?:, ([\w.]+))?\);')
armor_config_pattern = re.compile(r'''
[\s\t]*public (\w+)Config\(\) \{
[\s\t]*this\.enabled = (?:true|false);
[\s\t]*this\.toughness = (\d+\.\d+)f;(?:
[\s\t]*this\.helmetDurability = (\d+);)?(?:
[\s\t]*this\.helmetDefense = (\d+);)?(?:
[\s\t]*this\.chestplateDurability = (\d+);)?(?:
[\s\t]*this\.chestplateDefense = (\d+);)?(?:
[\s\t]*this\.leggingsDurability = (\d+);)?(?:
[\s\t]*this\.leggingsDefense = (\d+);)?(?:
[\s\t]*this\.bootsDurability = (\d+);)?(?:
[\s\t]*this\.bootsDefense = (\d+);)?''')

id_pos_dict = {
	"helmet": 4,
	"chestplate": 5,
	"leggings": 6,
	"boots": 7
}

class_pos_dict = {
	"helmet": 8,
	"chestplate": 9,
	"leggings": 10,
	"boots": 11
}

color_pos_dict = {
	"helmet": 26,
	"chestplate": 27,
	"leggings": 28,
	"boots": 29
}


def get_armor_models_dict():
	models_dict = {}

	with open(addon_models_path, 'r') as f:
		matches = armor_model_pattern.findall(f.read())
		for match in matches:
			models_dict[f'{modid}:{match[0]}'] = match[1]
	with open(mod_models_path, 'r') as f:
		matches = armor_model_pattern.findall(f.read())
		for match in matches:
			models_dict[f'magistuarmory:{match[0]}'] = match[1]

	return models_dict


def main():
	models_dict = get_armor_models_dict()

	armor_dict = {}

	with open(armor_types_path, "r") as f:
		matches = armor_type_pattern.findall(f.read())
		for match in matches:
			row = [""] * 30
			row[0] = match[0]
			row[1] = match[1]
			row[2] = match[2]
			row[3] = match[3]
			row[13] = match[4]
			row[22] = match[5]
			row[23] = match[6]
			row[24] = match[7]
			row[25] = models_dict.get(match[3], "")
			armor_dict[match[0].lower()] = row

	with open(items_path, "r") as f:
		matches = armor_item_pattern.findall(f.read())
		for match in matches:
			slot = match[3].lower()
			row = armor_dict[match[2].lower()]
			row[id_pos_dict[slot]] = match[1]
			row[class_pos_dict[slot]] = match[0]
			row[color_pos_dict[slot]] = match[4]

	with open(armor_config_path, "r") as f:
		matches = armor_config_pattern.findall(f.read())
		for match in matches:
			row = armor_dict[to_snake_case(match[0])]
			row[12] = match[1]
			row[17] = match[2]
			row[21] = match[3]
			row[16] = match[4]
			row[20] = match[5]
			row[15] = match[6]
			row[19] = match[7]
			row[14] = match[8]
			row[18] = match[9]

	for row in armor_dict.values():
		print("\t".join(row))



if __name__ == "__main__":
	main()