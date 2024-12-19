
def origin():
    from os import getlogin, mkdir,system

    name = getlogin()
    path = rf'C:\Users\{name}\AppData\Roaming\file'
    try:
        mkdir(path)
    except:
        work = True

    while work:
        print('Выбирите нужное действие')
        print('5.Выход')
        num = input()
        system('cls')
        if num == "5":
            work = False
        else:
            print('Не выбран пункт меню!!!')