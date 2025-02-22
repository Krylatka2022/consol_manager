# Функции для банковского счёта
"""- мой банковский счет;"""

"""
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз 
(задание учебное, после выхода из программы управлением счетом в главной программе 
сумму и историю покупок можно не запоминать);"""

# Инициализация баланса и списка покупок
def user_balanse():
    balance = 0
    purchase_history = []

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            add_amount = input('Введите сумму для пополнения счета: ')
            try:
                add_amount = float(add_amount)
            except ValueError:
                print("Неверная сумма. Попробуйте еще раз.")
                continue

            balance += add_amount
            print(f'Ваш текущий баланс: {balance}')

        elif choice == '2':
            purchase_amount = input('Введите сумму покупки: ')
            try:
                purchase_amount = float(purchase_amount)
            except ValueError:
                print("Неверная сумма. Попробуйте еще раз.")
                continue

            if purchase_amount > balance:
                print("Денег не хватает!")
                continue

            purchase_name = input("Введите название покупки: ")
            balance -= purchase_amount
            purchase_history.append((purchase_name, purchase_amount))
            print("Покупка совершена.")
            print(f'Остаток на счете: {balance}')

        elif choice == '3':
            print("\nИстория покупок:")
            if not purchase_history:
                print("Покупок не было.")
            else:
                for name, amount in purchase_history:
                    print(f"{name} - {amount}")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print('Неверный пункт меню. Попробуйте еще раз.')


# Если модуль запускается напрямую, запускаем управление счетом
if __name__ == "__main__":
    user_balanse()
