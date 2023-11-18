from random import randint
import logging


def get_barrels_amount():
    """
    Функция для получения количества бочонков в мешке. Проверяет данные на корректность.

    :return: int
    """
    try:
        n = int(input("Введите количество бочонков в мешочке: "))
        if n > 0:
            return n
        else:
            return False
    except Exception as error:
        return False


if __name__ == "__main__":
    print("Добро пожаловать в клуб любителей лото!")

    # Вводим число n пока не будет валидным
    n = get_barrels_amount()
    while not n:
        print("Ошибка! Введенное число должно быть натуральным.")
        n = get_barrels_amount()

    
