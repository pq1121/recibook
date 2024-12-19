def origin():
    work = True
    while work:
        print('Выбирите нужное действие')
        print('5.Выход')
        num = input()
        if num == "5":
            work = False
        else:
            print('Не выбран пункт меню!!!')