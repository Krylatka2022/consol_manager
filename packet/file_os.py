# Функции для создания, удаления, копирования папок и файлов
"""- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
"""
"""
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;

- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;

- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;

- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;

- посмотреть только папки
вывод только папок которые находятся в рабочей папке;

- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке;
"""
import os
import shutil

def create_folder():
    folder_name = input("Введите имя папки для создания: ")
    if os.path.exists(folder_name):
        print(f"Папка или файл '{folder_name}' уже существует.")
    else:
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' успешно создана.")

def delete_item():
    item_name = input("Введите имя файла или папки для удаления: ")
    if os.path.exists(item_name):
        # Если это папка – удаляем с содержимым, если файл – просто удаляем.
        if os.path.isdir(item_name):
            shutil.rmtree(item_name)
            print(f"Папка '{item_name}' успешно удалена.")
        else:
            os.remove(item_name)
            print(f"Файл '{item_name}' успешно удалён.")
    else:
        print(f"Папка или файл '{item_name}' не существует.")


def copy_item():
    item_name = input("Введите имя файла/папки для копирования: ")
    if not os.path.exists(item_name):
        print(f"Папка или файл '{item_name}' не существует.")
        return
    new_copy = input("Введите новое имя для копии: ")
    if os.path.exists(new_copy):
        print(f"Папка или файл с именем '{new_copy}' уже существует.")
        return
    # Копируем в зависимости от типа исходного объекта
    if os.path.isdir(item_name):
        shutil.copytree(item_name, new_copy)
    else:
        shutil.copy2(item_name, new_copy)
    print(f"'{item_name}' успешно скопирован в '{new_copy}'.")

def list_directory():
    items = os.listdir()
    if items:
        print("Содержимое рабочей директории:")
        for item in items:
            print(item)
    else:
        print("Рабочая директория пуста.")

def list_folders():
    items = os.listdir()
    folders = [item for item in items if os.path.isdir(item)]
    if folders:
        print("Список папок:")
        for folder in folders:
            print(folder)
    else:
        print("В рабочей директории нет папок.")

def list_files():
    items = os.listdir()
    files = [item for item in items if os.path.isfile(item)]
    if files:
        print("Список файлов:")
        for file in files:
            print(file)
    else:
        print("В рабочей директории нет файлов.")


def is_directory():
    current_dir = os.getcwd()
    print("Текущая рабочая директория:", current_dir)