def origin():
    from os import getlogin, mkdir, system, listdir, remove
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
        print('2.Список всех каталогов с рецептами')
        print('3.Удаление каталога')
        print('4.Добавление рецепта')
        print('5.Выход')
        num = input()
        system('cls')
        if num == "1":
            f_m.create_catalog(path)
            system('cls')
        elif num == "2":
            lst_file = listdir(path)
            f_m.lst_all_catalog(lst_file)
        elif num == "3":
            lst_file = listdir(path)
            f_m.lst_all_catalog(lst_file)
            tag = int(input("Введите номер каталога для удаления "))
            remove(f_m.del_catalog(path, lst_file, tag))
        elif num == "4":
            lst_file = listdir(path)
            f_m.lst_all_catalog(lst_file)
            tag_rec = int(input("Выберите номер каталога для добавления рецепта "))
            f_m.add_recipe(path, lst_file, tag_rec)
        elif num == "5":
            work = False
        else:
            print('Не выбран пункт меню!!!')