from utils import *
from paths import *
import os


def save_img(img, path):
	as_PilImg(img).save(path)


def execute_for_batch(images_dir, tasks, results_dir, naming_fn=None):
	for image_name in os.listdir(images_dir):
		img = Image.open(images_dir + '/' + image_name)
		for i, (task, args) in enumerate(tasks):
			img = task(img, *args)
		new_name = image_name if naming_fn is None else naming_fn(image_name)
		save_img(img, results_dir + '/' + new_name)
		print(new_name)


def merge_from_dirs(bg_dir, fg_dir, results_dir):
	for bg_img_name in os.listdir(bg_dir):
		bg_img = Image.open(bg_dir + '/' + bg_img_name)
		fg_img = Image.open(fg_dir + '/' + bg_img_name)
		img = trans_paste(bg_img, fg_img, 0, 0)
		as_PilImg(img).save(results_dir + '/' + bg_img_name)
		print(bg_img_name)


def main():
	# tasks = ((resize, [1503, 864]),)
	# 
	# tasks = ((round_down_channel, [3, 40]),)
	# 
	# tasks = ((convert_to_png, [], relocate_channel, [0, [3, ]]),)

	tasks = ((convert_to_png, []),)

	# tasks = ((convert_to_png, []),
	#          (clear_area, [5, 0, 6, 16]),
	# 		 (clear_area, [4, 10, 8, 6]),)

	# tasks = ((crop, [679, 322, 1248, 645]),)
	# 
	# tasks = ((crop, [405, 157, 1532, 805], remove_background, []),)

	execute_for_batch(images_dir, tasks, results_dir)


# files_tasks = ((replace_name, [("edge": "")]),)
# files_factory.execute_batch(results_dir, files_tasks, results_dir)


if __name__ == '__main__':
	main()