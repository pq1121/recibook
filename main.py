def run():
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
        print('4.Работа с рецептами')
        print('5.Выход')
        num = input()
        system('cls')
        if num == "1":
            f_m.create_catalog(path)
            system('cls')
        elif num == "2" or num == "3":
            lst_file = listdir(path)
            f_m.lst_all_catalog(lst_file)
            if num == "3":
                tag_del_cat = int(input("Введите номер каталога для удаления или 0 для отмены "))
                if tag_del_cat != 0:
                    remove(f_m.del_catalog(path, tag_del_cat))
                system('cls')
        elif num == "4":
            rec = True
            while rec:
                print('Выбирите нужное действие')
                print('1.Просмотр рецептов в каталоге')
                print('2.Добавление рецепта')
                print('3.Поиск рецепта по наименованию')
                print('4.Удаление рецепта')
                print('5.Редактирование рецепта')
                print('6.Возврат в предыдущее меню')
                print('7.Выход')
                num_sec = input()
                system('cls')
                if num_sec == "1" or num_sec == "4":
                    lst_file = listdir(path)
                    f_m.lst_all_catalog(lst_file)
                    tag_rec = int(input("Выберите номер каталога для просмотра рецептов "))
                    system('cls')
                    path_tag = f_m.output_recipe(path, lst_file, tag_rec)
                    if num_sec == "4":
                        tag_del_rec = int(input("Выберите номер рецепта для удаления "))
                        f_m.del_recipe(path_tag, tag_del_rec)
                        system('cls')
                elif num_sec == "2":
                    lst_file = listdir(path)
                    f_m.lst_all_catalog(lst_file)
                    tag_add_rec = int(input("Выберите номер каталога для добавления рецепта "))
                    system('cls')
                    f_m.add_recipe(path, lst_file, tag_add_rec)
                elif num_sec == "3":
                    pass
                elif num_sec == "5":
                    pass
                elif num_sec == "6":
                    rec = False
                elif num_sec == "7":
                    rec = False
                    work = False
                else:
                    print('Не выбран пункт меню!!!')
        elif num == "5":
            work = False
        else:
            print('Не выбран пункт меню!!!')