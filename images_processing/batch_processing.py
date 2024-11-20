from common_utils import *
from utils import *
from paths import *
import os


def save_img(img, path):
	as_PilImg(img).save(path)


def execute_for_batch(images_dir, tasks, results_dir, path_fn=None):
	for image_name in os.listdir(images_dir):
		img = Image.open(images_dir + '/' + image_name)
		for i, (task, args) in enumerate(tasks):
			img = task(img, *args)
		path = results_dir + '/' + image_name if path_fn is None else path_fn(image_name)
		save_img(img, path)
		print(path)


def merge_from_dirs(bg_dir, fg_dir, results_dir):
	for bg_img_name in os.listdir(bg_dir):
		bg_img = Image.open(bg_dir + '/' + bg_img_name)
		fg_img = Image.open(fg_dir + '/' + bg_img_name)
		img = trans_paste(bg_img, fg_img, 0, 0)
		as_PilImg(img).save(results_dir + '/' + bg_img_name)
		print(bg_img_name)


def main():
	tasks = ((convert_to_png, []))
	execute_for_batch(images_dir, tasks, results_dir)

# files_tasks = ((replace_name, [("edge": "")]),)
# files_factory.execute_batch(results_dir, files_tasks, results_dir)


if __name__ == '__main__':
	main()