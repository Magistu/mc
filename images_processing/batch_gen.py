from batch_processing import *


def main():
	for material in ('diamond', 'gold', 'netherite', 'stone', 'bronze', 'tin', 'silver', 'copper', 'iron',):
		tasks = ((convert_to_png, []), (replace_palette, ['tfc_copper', material]))
		execute_for_batch(images_dir, tasks, results_dir, lambda filename: 'images_2/' + filename.replace('copper_', '').replace('.png', '') + '/' + filename.replace('copper_', material + '_'))

	for dirname in all_from_dir('images_2'):
		tasks = ((convert_to_png, []), (copypaste_image, ['images_2/' + dirname + '.png', 0, 0, 64, 64, 0, 0]))
		execute_for_batch('images_2/' + dirname, tasks, results_dir)


if __name__ == '__main__':
	main()