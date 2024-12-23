def create_catalog(path):
    import datetime

    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    text = input('Введите название киталога ')
    path_add = path + rf'\{text},{now},0.rcb'

    open(path_add,'w')

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