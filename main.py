from filters import GreenFilter, RedFilter, BlueFilter, Inversion, Intensifier, Blur, Contour
from PIL import Image

import os


def check_user_input(input_message, error_message, correct_inputs, *args):
    """
    Проверяет, входит ли введенная пользователем информация в список обрабатываемых ответов
    @param correct_inputs: перечень обрабатываемых ответов пользователя
    @type correct_inputs:list
    @param input_message: сообщение при вводе информации пользователем
    @type input_message:str
    @param error_message:сообщение при вводе необрабатываемой информации пользователем
    @type error_message:str
    @param args:дополнительные обрабатываемые ответы пользователя
    @type args:tuple
    @return:введенный обрабатываемый ответ пользователя
    @rtype:str
    """
    for arg in args:
        correct_inputs.append(arg)
    user_input = input(input_message).lower()
    while user_input not in correct_inputs:
        print(error_message)
        user_input = input("Вводить здесь: ").lower()
    return user_input


def menu(image):
    """
    Запускает меню фильтров
    @param image: открытое изображение в формате RGB
    @type image: Image
    @return: сохраняет обработанное фильтром изображение или ничего не делает по выбору пользователя
    @rtype: None
    """

    # Фильтры и классы с методами обработки.
    filters = {
        "1": {
            "name": "Красный фильтр",
            "description": "Плавно усиливает красный оттенок на изображении.",
            "class_name": RedFilter(100)
        },
        "2": {
            "name": "Зелёный фильтр",
            "description": "Плавно усиливает зелёный оттенок на изображении.",
            "class_name": GreenFilter(100)
        },
        "3": {
            "name": "Синий фильтр",
            "description": "Плавно усиливает синий оттенок на изображении.",
            "class_name": BlueFilter(100)
        },
        "4": {
            "name": "Инверсия",
            "description": "Инвертирует значения цветов.",
            "class_name": Inversion()
        },
        "5": {
            "name": "Усиление",
            "description": "Приводит значения цветов к максимуму или минимуму в зависимости от границы.",
            "class_name": Intensifier(130)
        },
        "6": {
            "name": "Размытие",
            "description": "Размывает изображение.",
            "class_name": Blur()
        },
        "7": {
            "name": "Выделение контуров",
            "description": "Делает конутры объектов на изображении более чёткими.",
            "class_name": Contour()
        }
    }

    # Меню фильтров
    print("Меню фильтров:")
    message = ""
    for key, value in filters.items():
        message += f"{key}: {value['name']}\n"
    print(message)

    # Выбор фильтра и его применение
    filter_num = check_user_input("Выберите фильтр (или 0 для выхода):",
                                  "Номер фильтра неверен. Пожалуйста, проверьте правильность номера фильтра.",
                                  list(filters), "0")
    if filter_num == "0":
        print("Выход")
        return None

    # Вывод описания фильтра
    print(f"{filters[filter_num]['name']}:")
    print(f"{filters[filter_num]['description']}")

    # Применить фильтр к картинке? (Да/Нет): Да
    verify_filter_use = check_user_input("Применить фильтр к картинке? (Да/Нет):",
                                         "Ответ неверен. Пожалуйста, проверьте правильность ответа.",
                                         ["да", "нет"])

    if verify_filter_use == "да":
        print("Применяем фильтр")
        fltr = filters[filter_num]["class_name"]
        img = fltr.apply_filter(image)

        # Куда сохранить: /path/to/new_image.jpg
        path_to_save = input("Куда сохранить: ")
        img.save(path_to_save)


print("Добро пожаловать в фоторедактор!")

# Вывод меню фильтров через цикл
is_running = True
while is_running:
    # Запрос пути
    print("Введите путь к файлу, например: /path/to/image.jpg")
    path = input("Вводить здесь: ")
    # Проверка пути и открытие изображения
    while not os.path.exists(path):
        path = input("Файл не найден. Попробуйте ещё раз: ")
    img = Image.open(path).convert("RGB")

    # Вызов меню и отработка фильтра
    menu(img)

    # Ещё раз? (Да/Нет): Нет
    # проверяем ввод
    answer = check_user_input("Ещё раз? (да/нет): ", "Некорректный ввод. Попробуйте ещё раз: ", ["да", "нет"])
    is_running = answer == "да"

print("До свидания")
