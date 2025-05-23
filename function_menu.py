from __future__ import annotations
import function_files as f_f


ADD = 1
DELL = 2
EDIT = 3

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


def add_recipe(path: str, lst_catalog: list, target: int):
    import datetime

    """
    Добавления рецепта в каталог
    :param path: путь до папки с каталогами
    :param lst: список состоящий из каталогов в папке
    :param target: в какой каталог произвести запись
    :return:
    """

    name, compound, description, time, diff = check_add_recipe(lst_catalog, target)

    if name == 0:
        return 0
    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    path_rec = path + rf'\{lst_catalog[target - 1]}'

    data = f_f.open_catalog(path_rec)

    if not data:
        recipe = f"{name};{compound};{description};{time};{now};{diff}"

    else:
        recipe = f"\n{name};{compound};{description};{time};{now};{diff}"

    f_f.add_new_recipe(path_rec, recipe)
    rename_catalog(path_rec, ADD)
    successful_completion()


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

    elif value == DELL:
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
    successful_completion()

def check_catalog_name(path: str, name: str):

    for catalog in f_f.list_catalog(path):

        if (catalog.split(','))[0] == name:
            return 0

def input_catalog_name():
    return input('Введите название киталога или 0 для отмены ')


def search_recipe(path_folder: str, value: str):
    catalog_lst = f_f.list_catalog(path_folder)
    result_search = ''

    for i in range(len(catalog_lst)):
        path_open = rf"{path_folder}\{catalog_lst[i]}"
        recipe_lst = f_f.open_catalog(path_open).split('\n')

        for j in range(len(recipe_lst)):
            recipe = recipe_lst[j].split(';')

            if value in recipe[0]:
                result_search += f'Рецепт {recipe[0]} находится в каталоге {(catalog_lst[i].split(','))[0]}\n'

    if result_search:
        return result_search

    else:
        return 0


def edit_recipe(path_edit: str, target: int):

    data_lst = f_f.open_catalog(path_edit).split('\n')
    edit_recipe = check_edit_recipe(data_lst[target - 1])

    if edit_recipe != "0":
        data_lst[target - 1] = edit_recipe
        result = ''

        for rec in data_lst:
            result += f"{rec}\n"
        result = result[:-1]

        f_f.write_recipe(path_edit, result)
        rename_catalog(path_edit, EDIT)
        successful_completion()


def check_add_recipe(lst_catalog: list, target: int):
    from os import system

    lst_input = ['Введите название ', 'Введите состав ', 'Введите краткое описание ', 'Введите время приготовления ',
                 'Укажите сложность приготовления ']
    lst_info = []
    count = len(lst_input)
    print(f"Добавление рецепта в каталог {((lst_catalog[target - 1]).split(','))[0]} или введите 0 для отмены\n")

    while count > 0:

        for i in range(len(lst_input)):

            buff = input(lst_input[i])

            if buff == "0":
                return 0, 0, 0, 0, 0

            elif buff == '':
                system("cls")
                print(f"{lst_input[i]} не может быть пустым\n")
                print(
                    f"Добавление рецепта в каталог {((lst_catalog[target - 1]).split(','))[0]} или введите 0 для отмены\n")
                break

            else:
                lst_info.append(buff)
                count -= 1
    return lst_info[0], lst_info[1], lst_info[2], lst_info[3], lst_info[4]


def check_edit_recipe(recipe: str):
    import datetime

    lst_recipe = recipe.split(';')
    print("Чтобы оставить без изменений нажмите Enter или 0 для отмены\n")
    lst_edit = ['Введите название ', 'Введите состав ', 'Введите краткое описание ', 'Введите время приготовления ',
                 'Время установится автоматически Enter для продолжения', 'Укажите сложность приготовления ']
    lst_edit_recipe = []
    count = len(lst_edit)

    while count > 0:

        for i in range(len(lst_edit)):

            buff = input(lst_edit[i])

            if buff == "0":
                return "0"

            elif buff == '':
                lst_edit_recipe.append(lst_recipe[i])
                count -= 1

            else:
                lst_edit_recipe.append(buff)
                count -= 1
    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    return f"{lst_edit_recipe[0]};{lst_edit_recipe[1]};{lst_edit_recipe[2]};{lst_edit_recipe[3]};{now};{lst_edit_recipe[5]}"


def successful_completion() -> None:
    from os import system
    import time

    print("Успешно выполнено!")
    time.sleep(1.5)
    system("clr")