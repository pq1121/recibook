# Recibook
## Консольное приложение для хранения кулинарных рецептов

### Инструкция по установке и запуске
Склонировать репозиторий
```
git clone https://github.com/pq1121/recibook.git
```
```
Для начала работы необходимо запустить файл app.py
```

### Справочная информация
- Приложение предназначено для работы в операционной системе windows.
- Меню приложения состоит из главного (работа с каталогами) и подменю (работа с рецептами).
- Все команды вводятся с клавиатуры соответствующей цифры необходимого пункта меню.
- При первом запуске автоматически создается папка в которой будут хранится файлы для работы с приложением, по следующему пути
```
C:\Users\<Имя Пользователя>\AppData\Roaming\files_rcb
```
### Главное меню приложения
```
Выбирите нужное действие

1.Создание каталога рецептов
2.Список всех каталогов с рецептами
3.Удаление каталога
4.Работа с рецептами
5.Выход
```
### Подменю приложения
```
Выбирите нужное действие

1.Просмотр рецептов в каталоге
2.Добавление рецепта
3.Поиск рецепта по наименованию
4.Удаление рецепта
5.Редактирование рецепта
6.Возврат в предыдущее меню
7.Выход
```

### Основные возможности

1.**`Создание каталога рецептов`** Запрашивает имя каталога, создает каталог с расширением *.rcb для дальнейшего хранения в нем записей с рецептами.
```
Введите название киталога или 0 для отмены _
```
2.**`Список всех каталогов с рецептами`** Выводит список всех каталогов.
```
Список Каталогов с рецептами
1.Первое блюдо дата создания:20:00 10-05-2025 рецептов:1
2.Салаты дата создания:22:21 10-05-2025 рецептов:0

Выбирите нужное действие
...
```
3.**`Удаление каталога`** Выводит список всех каталогов, для выбора каталога на удаление.
```
Список Каталогов с рецептами
1.Первое блюдо дата создания:20:00 10-05-2025 рецептов:1
2.Салаты дата создания:22:21 10-05-2025 рецептов:0

Введите номер каталога для удаления или 0 для отмены _
```
4.**`Работа с рецептами`** Переход в подменю для работы с рецептами.

1. **`Просмотр рецептов в каталоге`** Выводит список всех каталогов, для выбора каталога с рецептами.
    ```
    Список Каталогов с рецептами
    1.Первое блюдо дата создания:20:00 10-05-2025 рецептов:1
    2.Салаты дата создания:22:21 10-05-2025 рецептов:0

    Выберите номер каталога для просмотра рецептов или 0 для отмены _
    ```
    ```
    1.Суп; Состав:вода, картофель, зелень; Описание:залить и варить; Время приготовления:25 мин; Дата создания:21-53_10-05-2025; Сложность:3

    Выбирите нужное действие
    ...
    ```
2. **`Добавление рецепта`** Выводит список всех каталогов, для выбора в какой необходимо добавить новый рецепт, далее запрашивает данные для заполнения рецепта.
    ```
    Добавление рецепта в каталог Первое блюдо или введите 0 для отмены

    Введите название Окрошка
    Введите состав колбаса, картофель, огурец
    Введите краткое описание нарезать и перемешать
    Введите время приготовления 25 мин
    Укажите сложность приготовления 2_
    ```
3. **`Поиск рецепта по наименованию`** Запрашивает название рецепта для поиска в каком каталоге он находится.
    ```
    Введите название рецепта для поиска или 0 для отмены _
    ```
    ```
    Рецепт Окрошка находится в каталоге Первое блюдо
    Рецепт Оливье находится в каталоге Салаты

    Выбирите нужное действие
    ...
    ```
4. **`Удаление рецепта`** Выводит список всех каталогов, для выбора каталога. Далее выводится список доступных для удаления рецептов.
    ```
    1.Суп; Состав:вода, картофель, зелень; Описание:залить и варить; Время приготовления:25 мин; Дата создания:21-53_10-05-2025; Сложность:3
    2.Окрошка; Состав:колбаса, картофель, огурец; Описание:нарезать и перемешать; Время приготовления:25 мин; Дата создания:22-34_10-05-2025; Сложность:2

    Выберите номер рецепта для удаления или 0 для отмены _
    ```
5. **`Редактирование рецепта`** Выводит список всех каталогов, для выбора каталога. Далее выводится список доступных для редактирования рецептов.
    ```
    1.Суп; Состав:вода, картофель, зелень; Описание:залить и варить; Время приготовления:25 мин; Дата создания:21-53_10-05-2025; Сложность:3
    2.Окрошка; Состав:колбаса, картофель, огурец; Описание:нарезать и перемешать; Время приготовления:25 мин; Дата создания:22-34_10-05-2025; Сложность:2

    Выберите номер рецепта для редактирования или 0 для отмены 1
    Чтобы оставить без изменений нажмите Enter или 0 для отмены

    Введите название _
    ```
6. **`Возврат в предыдущее меню`** Возвращает в главное меню.
	
7. **`Выход`** Выход из приложения.

5.**`Выход`** Выход из приложения.

### Особенности приложения

- Для отмены каких либо действий, кроме уже совершенных, введите **Ноль** с клавиатуры.
- При удалении не пустого каталога с рецептами предусмотрена допольнительная проверка.
- При редактировании рецепта, если необходимо оставить какое то поле без изменений нажмите клавишу **Enter**.
