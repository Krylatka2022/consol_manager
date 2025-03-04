# Функции для получения информации об операционной системе и создателе программы
"""- просмотр информации об операционной системе;
- создатель программы;"""
"""
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
"""
import sys
import platform


# def show_sys_info():
#     print("Информация об операционной системе:")
#     print("ОС:", platform.system())
#     print("Версия ОС:", platform.release())
#     print("Детальная версия:", platform.version())
#     print("Имя устройства:", platform.node())
#     print("Платформа (sys):", sys.platform)
#
#
# def show_creator_info():
#     print("Информация о создателе программы:")
#     print("Имя: Дарья Крушельницкая")
#     print("Контакт: dasha_fr_russia@mail.ru")


def show_sys_info():
    return (
        f"ОС: {platform.system()}\n"
        f"Версия ОС: {platform.release()}\n"
        f"Детальная версия: {platform.version()}\n"
        f"Имя устройства: {platform.node()}\n"
        f"Платформа (sys): {sys.platform}"
    )


def show_creator_info():
    return ("Имя: Дарья Крушельницкая"
            "\nКонтакт: dasha_fr_russia@mail.ru")


if __name__ == "__main__":
    while True:
        print("0. Выход")
        print("1. Инфо о системе")
        print("2. Инфо о создателе")

        choice = input("Выберите пункт меню: ")
        if choice == "0":
            sys.exit(0)
        elif choice == "1":
            print(show_sys_info())
        elif choice == "2":
            print(show_creator_info())
        else:
            print("Неверный пункт меню")
