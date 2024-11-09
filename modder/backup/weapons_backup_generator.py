import re

from modder.code_helper import to_snake_case
weapon_types_dict                   																			 = {"ahlspiess":"spear","barbed_club":"axe","bastard_sword":"longsword","blacksmith_hammer":"axe","claymore":"greatsword","club":"axe","concave_edged_halberd":"halberd","estoc":"longsword","flail":"axe","flame_bladed_sword":"greatsword","giant_lance":"lance","guisarme":"spear","heavy_mace":"axe","heavy_war_hammer":"axe","katzbalger":"sword","lochaber_axe":"longaxe","lucerne_hammer":"longaxe","morningstar":"axe","noble_sword":"longsword","pike":"spear","pitchfork":"spear","ranseur":"spear","rusted_bastard_sword":"longsword","rusted_heavy_mace":"axe","short_sword":"sword","stiletto":"dagger","zweihander":"greatsword","arming_sword_type_xiii":"sword","arming_sword_type_xiv":"sword","arming_sword_type_xv":"sword","battleaxe":"axe","billhook":"spear","boar_spear":"spear","broadaxe":"axe","cutlass":"longsword","dagger":"dagger","daneaxe":"longaxe","english_poleaxe":"halberd","executioners_sword":"greatsword","falchion":"longsword","fauchard":"spear","feder":"longsword","francisca_axe":"axe","french_halberd":"halberd","gallowglass_axe":"longaxe","german_greatsword":"greatsword","glaive":"spear","goudendag":"spear","grand_falchion":"longsword","italian_poleaxe":"halberd","lance":"lance","long_seax":"longsword","longsword":"longsword","messer_sword":"longsword","partisan":"spear","rapier":"longsword","rich_saxon_sword":"sword","rondel_dagger":"dagger","sabre":"sword","saxon_sword":"sword","scimitar":"longsword","scythe":"spear","short_seax":"sword","short_spear":"spear","sickle":"dagger","sidesword":"longsword","swiss_halberd":"halberd","training_sword":"sword","voulge":"spear","war_axe":"axe","war_hammer":"axe","welsh_guisarme":"spear","rogatina":"spear","rus_axe":"axe","rus_sword":"sword","winged_rogatina":"spear", "swordbreaker":"sword"}

modid = "magistuarmoryaddon"

generated_dir = 'generated'
weapons_config_path = f'backup/{generated_dir}/{modid}/WeaponsConfig.java'
weapon_types_path = f'backup/{generated_dir}/{modid}/AddonWeaponTypes.java'
items_path = f'backup/{generated_dir}/{modid}/AddonItems.java'

weapon_type_pattern = re.compile(r'(\w+) = new WeaponType\(WEAPONS_CONFIG\.\w+\.baseAttackDamage, WEAPONS_CONFIG\.\w+\.baseAttackSpeed, WEAPONS_CONFIG\.\w+\.bonusAttackReach, (\d+\.\d+)f, (\d+\.\d+)f, (\d+), WEAPONS_CONFIG\.\w+\.enabled\)(?:\.setTwoHanded\((\d+)\))?(\.setFlamebladed\(\))?(?:\.setMaxBlockDamage\((\d+\.\d+)f\))?(\.setHalberd\(\))?;')
weapon_item_pattern = re.compile(r'INSTANCE\.add(\w+)\("(\w+)", new Item\.Properties\(\), \w+\.(\w+), AddonWeaponTypes\.(\w+)\);')
weapons_config_pattern = re.compile(r'''public (\w+)Config\(\) \{
[\s\t]*this\.enabled = (?:true|false);
[\s\t]*this\.baseAttackDamage = (\d+\.\d+)f;
[\s\t]*this\.baseAttackSpeed = (\d+\.\d+)f;
[\s\t]*this\.bonusAttackReach = (\d+\.\d+)f;''')

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

def main():
	weapons_dict = {}

	with open(weapon_types_path, "r") as f:
		matches = weapon_type_pattern.findall(f.read())
		for match in matches:
			row = [""] * 17
			row[0] = match[0]
			row[1] = modid
			row[5] = weapon_types_dict.get(match[0].lower(), "???")
			row[9] = match[1]
			row[10] = match[2]
			row[11] = match[3]
			row[12] = match[4] if match[4] else "0"
			row[16] = "1" if match[5] else "0"
			row[13] = match[6] if match[6] else "0"
			row[14] = "1" if match[7] else "0"
			weapons_dict[match[0].lower()] = row

	with open(items_path, "r") as f:
		matches = weapon_item_pattern.findall(f.read())
		for match in matches:
			row = weapons_dict[match[3].lower()]
			if row[3]:
				row[3] += "," + match[2].lower()
				continue
			row[15] = "1" if "Lance" in match[0] else "0"
			material = match[2].lower()
			row[2] = re.sub(fr'^{material}_', '', match[1])
			row[3] = material
			row[4] = "1" if row[2].startswith(match[2].lower() + "_") else "0"

	with open(weapons_config_path, "r") as f:
		matches = weapons_config_pattern.findall(f.read())
		for match in matches:
			row = weapons_dict[to_snake_case(match[0])]
			row[6] = match[1]
			row[7] = match[2]
			row[8] = match[3]

	for row in weapons_dict.values():
		print("\t".join(row))



if __name__ == "__main__":
	main()