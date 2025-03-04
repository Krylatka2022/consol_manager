"""
для тестирования функций консольного файлового менеджера
"""
# import pytest
import os
import shutil
from packet.file_os import create_folder, delete_item, copy_item, list_directory, list_folders, list_files, is_directory
from packet.sys_info import show_sys_info, show_creator_info
from packet.victory import check_birth_year, check_birth_day
from packet.bank import add_funds, can_purchase, make_purchase


# Функции для создания, удаления, копирования папок и файлов
def test_create_folder():
    folder_name = 'test_folder'
    # Создаём папку и проверяем результат
    result = create_folder(folder_name)
    assert result == f"Папка '{folder_name}' успешно создана."
    assert os.path.isdir(folder_name)
    os.rmdir(folder_name)  # Удаляем папку


def test_delete_item():
    # Создаём файл
    test_file = 'test_file.txt'
    with open(test_file, 'w') as f:
        f.write("Test content")

    # Проверяем удаление файла
    result = delete_item(test_file)
    assert result == f"Файл '{test_file}' успешно удалён."
    assert not os.path.exists(test_file)

    # Создаём папку
    test_folder = 'test_folder'
    os.mkdir(test_folder)

    # Проверяем удаление папки
    result = delete_item(test_folder)
    assert result == f"Папка '{test_folder}' успешно удалена."
    assert not os.path.isdir(test_folder)


def test_copy_item():
    test_file = 'test_file.txt'
    # Создаём файл
    with open(test_file, 'w') as f:
        f.write("Test content")

    # Копируем файл
    copy_name = 'test_file_copy.txt'
    result = copy_item(test_file, copy_name)
    assert result == f"'{test_file}' успешно скопирован в '{copy_name}'."
    assert os.path.exists(copy_name)
    os.remove(copy_name)  # Удаляем копию


def test_list_directory():
    # Создаём файлы и папки
    test_file = 'test_file.txt'
    os.mkdir('test_folder')
    with open(test_file, 'w') as f:
        f.write("Test content")

    # Проверяем вывод содержимого директории
    result = list_directory()
    assert 'test_file.txt' in result
    assert 'test_folder' in result

    # Удаляем тестовые файлы и папки
    os.remove(test_file)
    shutil.rmtree('test_folder')


def test_list_folders():
    # Создаём папку
    test_folder = 'test_folder'
    os.mkdir(test_folder)

    # Проверяем список папок
    result = list_folders()
    assert test_folder in result

    # Удаляем папку
    shutil.rmtree(test_folder)


def test_list_files():
    # Создаём файл
    test_file = 'test_file.txt'
    with open(test_file, 'w') as f:
        f.write("Test content")

    # Проверяем список файлов
    result = list_files()
    assert test_file in result

    # Удаляем файл
    os.remove(test_file)


def test_is_directory():
    # Проверяем текущую директорию
    result = is_directory()
    assert "Текущая рабочая директория:" in result  # Проверяем, что строка начинается с этой фразы
    assert os.getcwd() in result  # Проверяем, что текущая рабочая директория содержится в строке

# Информация про ОС
def test_get_creator_info():
    assert show_creator_info() == ("Имя: Дарья Крушельницкая"
                                   "\nКонтакт: dasha_fr_russia@mail.ru")


def test_get_sys_info():
    assert isinstance(show_sys_info(), str)  # Проверяем, что вернется строка


# Викторина

def test_check_birth_year():
    assert check_birth_year('1799') is True
    assert check_birth_year('1800') is False


def test_check_birth_day():
    assert check_birth_day('6') is True
    assert check_birth_day('5') is False


# Банк
def test_add_funds():
    # Тестируем, что баланс корректно пополняется
    assert add_funds(0, 100) == 100
    assert add_funds(50, 25) == 75


def test_can_purchase():
    # Если средств хватает, функция возвращает True
    assert can_purchase(100, 50) is True
    # Если средств недостаточно, возвращает False
    assert can_purchase(100, 150) is False


def test_make_purchase_success():
    # При успешной покупке баланс уменьшается, а история покупок обновляется
    balance, history = make_purchase(100, [], 40, "Книга")
    assert balance == 60
    assert history == [("Книга", 40)]


def test_make_purchase_insufficient_funds():
    # При попытке покупки, когда средств недостаточно, функция возвращает сообщение об ошибке.
    result = make_purchase(30, [], 50, "Дорогая покупка")
    assert result == "Ошибка: Недостаточно средств для покупки"


def test_make_purchase_success():
    # При успешной покупке функция возвращает кортеж с новым балансом и обновленной историей покупок.
    new_balance, new_history = make_purchase(100, [("Покупка1", 20)], 30, "Покупка2")
    assert new_balance == 70  # 100 - 30 = 70
    assert new_history == [("Покупка1", 20), ("Покупка2", 30)]
