from __future__ import annotations
import function_files as f_f


ADD = 1
DELL = 2

def create_catalog(path: str, name: str):
    import datetime

    now = datetime.datetime.now().strftime("%H_%M %d-%m-%Y")
    path_add_catalog = path + rf'\{name},{now},0.rcb'

    open(path_add_catalog, 'w')


def lst_all_catalog(lst: list):

    if len(lst) != 0:
        print("Список Каталогов с рецептами")

        for i in range(len(lst)):
            lst_new = lst[i].split(',')
            print(f'{i+1}.{lst_new[0]} дата создания:{lst_new[1].replace("_", ":")} рецептов:{lst_new[2].replace(".rcb", "")}')
        print()

    else:
        return 0
    return 1


def del_catalog(path: str, target: int):
    from os import stat

    lst = f_f.list_catalog(path)
    path_del = path + rf'\{lst[target - 1]}'

    if stat(path_del).st_size != 0:
        print(f'В каталоге {((lst[target - 1]).split(','))[0]} есть рецепты\n')

        while True:
            del_del = input('Для подтверждения удаления каталога с рецептами введите 1 или 0 для отмены удаления ')

            if del_del == "1":
                return path_del

            elif del_del == "0":
                return 0

    else:
        return path_del


def add_recipe(path: str, lst: list, target: int):
    from os import system
    import datetime
    """
    Добавления рецепта в каталог
    :param path: путь до папки с каталогами
    :param lst: список состоящий из каталогов в папке
    :param target: в какой каталог произвести запись
    :return:
    """

    lst_input = ['Введите название ', 'Введите состав ', 'Введите краткое описание ', 'Введите время приготовления ',
                 'Укажите сложность приготовления ']
    lst_info = []
    count = len(lst_input)
    print(f"Добавление рецепта в каталог {((lst[target - 1]).split(','))[0]} или введите 0 для отмены\n")

    while count > 0:

        for i in range(len(lst_input)):

            buff = input(lst_input[i])

            if buff == "0":
                return 0

            elif buff == '':
                system("cls")
                print(f"{lst_input[i]} не может быть пустым\n")
                print(f"Добавление рецепта в каталог {((lst[target - 1]).split(','))[0]} или введите 0 для отмены\n")
                break

            else:
                lst_info.append(buff)
                count -= 1

    name, compound, description, time, diff = lst_info[0], lst_info[1], lst_info[2], lst_info[3], lst_info[4]
    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    path_rec = path + rf'\{lst[target - 1]}'

    data = f_f.open_catalog(path_rec)

    if not data:
        recipe = f"{name};{compound};{description};{time};{now};{diff}"

    else:
        recipe = f"\n{name};{compound};{description};{time};{now};{diff}"

    f_f.add_new_recipe(path_rec, recipe)
    rename_catalog(path_rec, ADD)


def rename_catalog(path: str, value: int):
    from os import rename
    """
    Изменение имени каталога
    :param target: выбор каталога
    :return:
    """
    lst = path.replace('.rcb', '').split(',')

    if value == ADD:
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

    data_lst = f_f.open_catalog(path_open).split('\n')

    for i in range(len(data_lst)):
        new_lst = data_lst[i].split(';')
        print(f'{i+1}.{new_lst[0]}; Состав:{new_lst[1]}; Описание:{new_lst[2]}; Время приготовления:{new_lst[3]};'
              f' Дата создания:{new_lst[4]}; Сложность:{new_lst[5]}')
    print()
    return path_open


def del_recipe(path: str, target: int):
    data_lst = f_f.open_catalog(path).split('\n')

    data_lst.remove(data_lst[target - 1])
    result = ''

    for rec in data_lst:
        result += f"{rec}\n"
    result = result[:-1]

    f_f.write_recipe(path, result)
    rename_catalog(path, DELL)

def check_catalog_name(path: str, name: str):
    for catalog in f_f.list_catalog(path):
        if (catalog.split(','))[0] == name:
            return 0

def input_catalog_name():
    return input('Введите название киталога или 0 для отмены ')