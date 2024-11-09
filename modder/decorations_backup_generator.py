import re

modid = "magistuarmoryaddon"

generated_dir = 'generated'
addon_models_path = f'{generated_dir}/{modid}/AddonModels.java'
mod_models_path = 'generated/magistuarmoryaddon/ModModels.java'
items_path = f'{generated_dir}/{modid}/AddonItems.java'

layer_pattern = re.compile(r'(\w+) = (\w+)\.createLayer\(\);')
decoration_model_pattern = re.compile(r'INSTANCE\.addDecorationModel\("(\w+)", (?:(\w+)::createLayer|\(\) -> (\w+))\);')
decoration_item_pattern = re.compile(r'INSTANCE\.add\w+\("(\w+)_decoration", \(\) -> new (\w+)\(new ResourceLocation\(\w+\.ID, "\w+"\), new Item\.Properties\(\), ArmorItem\.Type\.(\w+)(?:, ([\w.]+))?\)\);')
wearable_decoration_item_pattern = re.compile(r'INSTANCE\.add(\w*Wearable\w*)\("(\w+)_decoration", AddonArmorTypes.(\w+), ArmorItem\.Type\.(\w+), new Item\.Properties\(\)(?:, ([\w.]+))?\);')


def get_layers_dict():
	layers_dict = {}

	with open(addon_models_path, 'r') as f:
		matches = layer_pattern.findall(f.read())
		for match in matches:
			layers_dict[match[0]] = f'{match[1]}'
	with open(mod_models_path, 'r') as f:
		matches = layer_pattern.findall(f.read())
		for match in matches:
			layers_dict[match[0]] = f'{match[1]}'

	return layers_dict


def get_decoration_models_dict():
	layers_dict = get_layers_dict()
	models_dict = {}

	with open(addon_models_path, 'r') as f:
		matches = decoration_model_pattern.findall(f.read())
		for match in matches:
			models_dict[f'{modid}:{match[0]}'] = match[1] if match[1] else layers_dict[match[2]]
	with open(mod_models_path, 'r') as f:
		matches = decoration_model_pattern.findall(f.read())
		for match in matches:
			models_dict[f'magistuarmory:{match[0]}'] = match[1] if match[1] else layers_dict[match[2]]

	return models_dict


def main():
	decorations_dict = {}
	models_dict = get_decoration_models_dict()

	with open(items_path, "r") as f:
		contents = f.read()
		matches = decoration_item_pattern.findall(contents)
		for match in matches:
			row = [""] * 7
			id = match[0]
			row[0] = match[0]
			row[2] = match[1]
			row[1] = modid
			row[5] = ''
			row[3] = match[2]
			row[4] = models_dict[f'{modid}:{id}']
			row[6] = match[3]
			decorations_dict[id] = row
		matches = wearable_decoration_item_pattern.findall(contents)
		for match in matches:
			row = [""] * 7
			id = match[1]
			row[2] = match[0]
			row[0] = match[1]
			row[5] = match[2]
			row[1] = modid
			row[3] = match[3]
			row[4] = models_dict[f'{modid}:{id}']
			row[6] = match[4]
			decorations_dict[id] = row

	for row in decorations_dict.values():
		print("\t".join(row))



if __name__ == "__main__":
	main()