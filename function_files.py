from __future__ import annotations


def list_catalog(path: str):
    from os import listdir

    return listdir(path)

def open_catalog(path_folder: str):

    with open(path_folder, 'r', encoding='utf8') as file:
        data = file.read()

    return data

def write_recipe(path_folder: str, data: str):

    with open(path_folder, 'w', encoding='utf8') as file:
        file.write(data)

def add_new_recipe(path_folder: str, data: str):

    with open(path_folder, 'a', encoding='utf8') as file:
        file.write(data)
