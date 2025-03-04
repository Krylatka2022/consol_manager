# Функции для банковского счёта
"""- мой банковский счет;"""

"""
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз 
(задание учебное, после выхода из программы управлением счетом в главной программе 
сумму и историю покупок можно не запоминать);"""


# Инициализация баланса и списка покупок
"""
    Интерактивная функция для управления счетом.
    Использует чистые функции (add_funds, can_purchase, make_purchase) для изменения состояния.
"""
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

            # balance += add_amount
            # Используем функцию add_funds для обновления баланса.
            balance = add_funds(balance, add_amount)
            print(f'Ваш текущий баланс: {balance}')

        elif choice == '2':
            purchase_amount = input('Введите сумму покупки: ')
            try:
                purchase_amount = float(purchase_amount)
            except ValueError:
                print("Неверная сумма. Попробуйте еще раз.")
                continue

            # if purchase_amount > balance:
            # Проверяем, достаточно ли средств, используя функцию can_purchase.
            if not can_purchase(balance, purchase_amount):
                print("Денег не хватает!")
                continue

            purchase_name = input("Введите название покупки: ")

            # balance -= purchase_amount
            # purchase_history.append((purchase_name, purchase_amount))
            # print("Покупка совершена.")
            # print(f'Остаток на счете: {balance}')

            # Пытаемся совершить покупку через функцию make_purchase.
            result = make_purchase(balance, purchase_history, purchase_amount, purchase_name)
            if isinstance(result, str):
                # Если вернулась строка, значит произошла ошибка.
                print(result)
            else:
                balance, purchase_history = result
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


""" Функция для пополнения баланса
   Возвращает новый баланс после пополнения."""


def add_funds(balance: float, add_amount: float) -> float:
    """

    :param balance: Текущий баланс
    :param add_amount: Сумма, которую пользователь хочет добавить
    :return: Новый баланс, полученный в результате прибавления add_amount к balance
    """
    return balance + add_amount


""" Функция для совершения покупки
Проверяет, достаточно ли средств для покупки."""


def can_purchase(balance: float, purchase_amount: float) -> bool:
    """

    :param balance: Текущий баланс
    :param purchase_amount: Стоимость покупки,
    :return: True, если баланс достаточен для покупки (то есть purchase_amount меньше или равен balance),
    """
    return purchase_amount <= balance


""" Функция для проверки возможности покупки.
Пытается совершить покупку. Если средств недостаточно, возвращает сообщение об ошибке.
Иначе возвращает кортеж: (новый баланс, обновлённая история покупок)."""

def make_purchase(balance: float, purchase_history: list, purchase_amount: float, purchase_name: str):
    """
    :param balance: Текущий баланс.
    :param purchase_history: Список с историей покупок.
    :param purchase_amount: Сумма покупки.
    :param purchase_name: Название покупки.
    :return: "Ошибка: Недостаточно средств для покупки" или (новый баланс, новый список покупок).
    """
    if purchase_amount > balance:
        return "Ошибка: Недостаточно средств для покупки"
    new_balance = balance - purchase_amount
    new_history = purchase_history.copy()
    new_history.append((purchase_name, purchase_amount))
    return new_balance, new_history


# Если модуль запускается напрямую, запускаем управление счетом
if __name__ == "__main__":
    user_balanse()
