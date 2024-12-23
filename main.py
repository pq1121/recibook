
def origin():
    from os import getlogin, mkdir, system
    import function_menu as f_m
    name = getlogin()
    path = rf'C:\Users\{name}\AppData\Roaming\file'
    try:
        mkdir(path)
        work = True
    except:
        work = True

    while work:
        print('Выбирите нужное действие')
        print('1.Создание каталога рецептов')
        print('5.Выход')
        num = input()
        system('cls')
        if num == "1":
            f_m.create_catalog(path)
            system('cls')
        elif num == "5":
            work = False
        else:
            print('Не выбран пункт меню!!!')