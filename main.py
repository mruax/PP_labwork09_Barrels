from random import randint
import logging


def get_barrels_amount():
    """
    Функция для получения количества бочонков в мешке. Проверяет данные на корректность.

    :return: int
    """
    n = input("Введите количество бочонков в мешочке: ")
    try:
        n = int(n)
        if n > 0:
            return n
        else:
            logging.error(f"Incorrect input data. n = {n}. Error: not natural number")
            return False
    except Exception as error:
        logging.error(f"Incorrect input data. n = {n}. Error: {error}")
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logs/barrels.log",
                        filemode="w", format="%(asctime)s %(levelname)s %(message)s")

    print("Добро пожаловать в клуб любителей лото!")

    # Вводим число n пока не будет валидным
    n = get_barrels_amount()
    while not n:
        print("Ошибка! Введенное число должно быть натуральным.")
        n = get_barrels_amount()
    logging.info(f"Input data n = {n}.")

