import os

from function_files import list_catalog

add = 1
dell = 2
def create_catalog(path: str, name: str):
    import datetime

    now = datetime.datetime.now().strftime("%H_%M %d-%m-%Y")
    path_add = path + rf'\{name},{now},0.rcb'

    open(path_add, 'w')

def lst_all_catalog(lst: list):
    if len(lst) != 0:
        print("Список Каталогов с рецептами")
        for i in range(len(lst)):
            lst_new = lst[i].split(',')
            print(f'{i+1}.{lst_new[0]} дата создания:{lst_new[1].replace("_", ":")} рецептов:{lst_new[2].replace(".rcb","")}')
        print()
    else:
        print("Каталоги с рецептами отсутствуют")

def del_catalog(path: str, target: int):
    lst_all_catalog(list_catalog(path))
    if target == 0:
        return 0
    else:
        lst = list_catalog(path)
        path_del = path + rf'\{lst[target - 1]}'
        return path_del

def add_recipe(path: str, lst: list, target: int):
    import datetime
    """
    Добавления рецепта в каталог
    :param path: путь до папки с каталогами
    :param lst: список состоящий из каталогов в папке
    :param target: в какой каталог произвести запись
    :return:
    """
    name = input('Введите название рецепта ')
    compound = input('Введите состав рецепта ')
    description = input('Введите краткое описание рецепта ')
    time = input('Введите время приготовления ')
    diff = input('Укажите сложность приготовления ')
    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    path_rec = path + rf'\{lst[target - 1]}'
    with open(path_rec, 'r', encoding='utf8') as file:
        data = file.read()
    if not data:
        recipe = f"{name};{compound};{description};{time};{now};{diff}"
    else:
        recipe = f"\n{name};{compound};{description};{time};{now};{diff}"
    with open(path_rec, 'a', encoding='utf8') as file:
        file.write(recipe)
    rename_catalog(path_rec, add)

def rename_catalog(path: str, value: int):
    from os import rename
    """
    Изменение имени каталога
    :param target: выбор каталога
    :return:
    """
    lst = path.replace('.rcb', '').split(',')
    if value == add:
        lst[2] = str(int(lst[2]) + 1)
    else:
        lst[2] = str(int(lst[2]) - 1)
    new_path = f"{lst[0]},{lst[1]},{lst[2]}.rcb"
    rename(path, new_path)

def output_recipe(path: str, lst: list, target: int):
    from os import stat

    path_open = path + rf'\{lst[target - 1]}'
    if stat(path_open).st_size == 0:
        print(f'В каталоге {((lst[target - 1]).split(','))[0]} рецепты отсутствуют\n')
        return 0
    with open(path_open, 'r', encoding='utf8') as file:
        data_lst = file.read().split('\n')

    for i in range(len(data_lst)):
        new_lst = data_lst[i].split(';')
        print(f'{i+1}.{new_lst[0]}; Состав:{new_lst[1]}; Описание:{new_lst[2]}; Время приготовления:{new_lst[3]};'
              f' Дата создания:{new_lst[4]}; Сложность:{new_lst[5]}')
    print()
    return path_open

def del_recipe(path: str, target: int):
    with open(path, 'r', encoding='utf8') as file:
        data_lst = file.read().split('\n')

    data_lst.remove(data_lst[target - 1])
    result = ''
    for rec in data_lst:
        result += f"{rec}\n"
    result = result[:-1]

    with open(path, 'w', encoding='utf8') as file:
        file.write(result)
    rename_catalog(path, dell)