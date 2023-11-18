from random import choice
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


def get_random_barrel(barrels):
    """
    Достает случайный бочонок из мешка, добавляет в стэк и удаляет из мешка.

    :param barrels: list - мешок с бочонками
    :return: bool
    """
    if barrels:
        _ = input("Нажмите клавишу Enter для того, чтобы достать бочонок ")

        barrel = choice(barrels)
        print(f"Выпал бочонок с номером {barrel}!")
        logging.info(f"Get random barrel = {barrel}.")

        stack.append(barrel)
        del barrels[barrels.index(barrel)]
        logging.info(f"Added {barrel} to stack. Removed {barrel} from barrels.")
        return True
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logs/barrels.log",
                        filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    logging.info("Program started")
    print("Добро пожаловать в клуб любителей лото!")

    # Вводим число n пока не будет валидным
    n = get_barrels_amount()
    while not n:
        print("Ошибка! Введенное число должно быть натуральным.")
        n = get_barrels_amount()
    logging.info(f"Input data n = {n}.")

    barrels = list(range(1, n + 1))
    logging.info(f"Created list with {n} elements from 1 to {n}.")

    stack = []
    logging.info("Created empty stack list")

    # Пока есть бочки в мешке достаем случайные
    while get_random_barrel(barrels):
        get_random_barrel(barrels)

    print("Мешок пуст!")
    print("Бочонки доставались в следующем порядке:")
    print(*stack)
    logging.info(f"Stack list = {stack}")
    logging.info("Program ended")
