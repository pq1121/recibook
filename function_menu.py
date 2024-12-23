def create_catalog(path):
    import datetime

    now = datetime.datetime.now().strftime("%H-%M_%d-%m-%Y")
    text = input('Введите название киталога ')
    path_add = path + rf'\{text},{now},0.rcb'

    open(path_add,'w')