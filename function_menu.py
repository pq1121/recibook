def create_catalog(path):
    import datetime

    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    text = input('Введите название киталога ')
    path_add = path + rf'\{text},{now},0.rcb'

    open(path_add, 'w')

def lst_all_catalog(lst: list):
    if len(lst) != 0:
        print("Список Каталогов с рецептами")
        for i in range(len(lst)):
            lst_new = lst[i].split(',')
            print(f'{i+1}.{lst_new[0]}')
    else:
        print("Каталоги с рецептами отсутствуют")

def del_catalog(path: str,lst: list,target: int):
    path_del = path + rf'\{lst[target - 1]}'
    return path_del

def add_recipe(path: str,lst: list, target: int):
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
        recipe = f"{name}_{compound}_{description}_{time}_{now}_{diff}"
    else:
        recipe = f"\n{name}_{compound}_{description}_{time}_{now}_{diff}"
    with open(path_rec, 'a', encoding='utf8') as file:
        file.write(recipe)