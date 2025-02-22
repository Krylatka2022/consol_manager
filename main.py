import packet.file_os as file_os
import packet.sys_info as sys_info
import packet.victory as game
import packet.bank as bank

def main():
    while True:
        print("\nКонсольный файловый менеджер")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Информация об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Моя рабочая директория сейчас")
        print("12. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            file_os.create_folder()
        elif choice == "2":
            file_os.delete_item()
        elif choice == "3":
            file_os.copy_item()
        elif choice == "4":
            file_os.list_directory()
        elif choice == "5":
            file_os.list_folders()
        elif choice == "6":
            file_os.list_files()
        elif choice == "7":
            sys_info.show_sys_info()
        elif choice == "8":
            sys_info.show_creator_info()
        elif choice == "9":
            game.ask_pushkin()
        elif choice == "10":
            bank.user_balanse()
        elif choice == "11":
            file_os.is_directory()
        elif choice == "12":
            print("Выход из программы...")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()