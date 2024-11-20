import os
import json


def replace_data(path, replaces):
    filename = path.split('/')[-1]
    if filename.split('.')[-1] != 'json':
        return
    with open(path, 'r') as f:
        data = f.read()
    for r in replaces.items():
        data = data.replace(r[0], r[1])
    with open(path, 'w') as f:
        f.write(data)


def remove_keys(path, keys):
    filename = path.split('/')[-1]
    if filename.split('.')[-1] != 'json':
        return
    with open(path, 'r') as f:
        data = json.load(f)
    for key in keys:
        if key in data.keys():
            data.pop(key)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def rename(path, new_path):
    if path != new_path and os.path.exists(new_path):
        os.remove(new_path)
    os.rename(path, new_path)


def replace_name(path, replaces):
    new_path = path
    for replace in replaces.items():
        path_array = new_path.split('/')
        filename = path_array[-1]
        file_dir = '/'.join(path_array[:-1])
        new_path = file_dir + '/' + filename.replace(replace[0], replace[1])
    rename(path, new_path)


def add_to_name(path, prefix, suffix=""):
    path_array = path.split('/')
    filename = path_array[-1]
    filename_ext = filename.split('.')[-1]
    name = '.'.join(filename.split('.')[:-1])
    file_dir = '/'.join(path_array[:-1])
    new_path = file_dir + '/' + prefix + name + suffix + '.' + filename_ext
    rename(path, new_path)
