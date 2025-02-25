def run():
    from os import getlogin, mkdir, system, listdir, remove, path

    import function_menu as f_m

    name = getlogin()
    path_folder_catalog = rf'C:\Users\{name}\AppData\Roaming\files_rcb'

    if not path.exists(path_folder_catalog):
        mkdir(path_folder_catalog)
        work = True
    else:
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
            name = input('Введите название киталога или 0 для отмены ')

            while True:

                if name == "":
                    system('cls')
                    print("Название каталога не может быть пустым")
                    name = input('Введите название киталога или 0 для отмены ')

                elif name != "0":
                    f_m.create_catalog(path_folder_catalog, name)
                    break
                else:
                    break
            system('cls')

        elif num == "2" or num == "3":
            lst_file = listdir(path_folder_catalog)

            if f_m.lst_all_catalog(lst_file):

                if num == "3":
                    tag_del_cat = int(input("Введите номер каталога для удаления или 0 для отмены "))
                    system('cls')
                    if tag_del_cat != 0:

                        check = f_m.del_catalog(path_folder_catalog, tag_del_cat)
                        if check != 0:
                            remove(check)
                    system('cls')
            else:
                print("Каталоги с рецептами отсутствуют\n")

        elif num == "4":
            lst_file = listdir(path_folder_catalog)
            if f_m.lst_all_catalog(lst_file):
                system('cls')
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
                        lst_file = listdir(path_folder_catalog)
                        f_m.lst_all_catalog(lst_file)
                        tag_rec = int(input("Выберите номер каталога для просмотра рецептов или 0 для отмены "))
                        system('cls')

                        if tag_rec != 0:
                            system('cls')
                            path_tag = f_m.output_recipe(path_folder_catalog, lst_file, tag_rec)

                            if num_sec == "4" and path_tag != 0:
                                tag_del_rec = int(input("Выберите номер рецепта для удаления или 0 для отмены "))

                                if tag_del_rec != 0:
                                    f_m.del_recipe(path_tag, tag_del_rec)
                                system('cls')

                    elif num_sec == "2":

                        lst_file = listdir(path_folder_catalog)
                        f_m.lst_all_catalog(lst_file)
                        tag_add_rec = int(input("Выберите номер каталога для добавления рецепта или 0 для отмены "))

                        if tag_add_rec != 0:
                            system('cls')
                            f_m.add_recipe(path_folder_catalog, lst_file, tag_add_rec)
                        system('cls')

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

            else:
                print("Для добавления рецептов необходимо создать один каталог\n")

        elif num == "5":
            work = False

        else:
            print('Не выбран пункт меню!!!')