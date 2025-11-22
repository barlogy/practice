#!/usr/bin/python
import numpy as np
from typing import Callable, Optional, List


def random_predict(number: int = 1, predict: Optional[int] = None) -> int:
    """
    Угадывает число случайным образом.
    Args:
        number (int, optional): Загаданное число. По умолчанию 1.
        predict (int, optional): Первоначальная догадка (не используется в этом методе).
    Returns:
        int: Количество попыток, потребовавшихся для угадывания
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # генерируем случайное число
        if number == predict_number:
            break  # выход из цикла при угадывании
    return count


def binary_search_predict(number: int, predict: Optional[int] = None) -> int:
    """
    Угадывает число с использованием алгоритма бинарного поиска.
    Args:
        number (int): Загаданное число
        predict (int, optional): Первоначальная догадка. Если не указана, используется 50.
    Returns:
        int: Количество попыток, потребовавшихся для угадывания
    """
    low, high = 1, 100
    # If predict is None or out of range, use the middle value
    if predict is None or not (low <= predict <= high):
        current_guess = (low + high) // 2
    else:
        current_guess = predict
    count = 1

    while low <= high:
        if current_guess == number:
            break
        elif current_guess < number:
            low = current_guess + 1
        else:
            high = current_guess - 1

        # Следующая догадка по бинарному поиску
        current_guess = (low + high) // 2
        count += 1

    return count


def score_game(predict_func: Callable[[int, Optional[int]], int],
               fix_seed: bool = False) -> int:
    """
    Оценивает среднее количество попыток для угадывания числа за 1000 подходов.
    Args:
        predict_func (Callable): Функция угадывания числа
        fix_seed (bool, optional): Фиксировать seed для воспроизводимости. По умолчанию False.
    Returns:
        int: Среднее количество попыток
    """
    count_ls: List[int] = []
    if fix_seed:
        np.random.seed(1)  # фиксируем сид для воспроизводимости

    # Генерируем массив чисел для тестирования
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        # Генерируем случайную начальную догадку для алгоритма
        initial_guess = np.random.randint(1, 101)
        count_ls.append(predict_func(number, initial_guess))

    score = int(np.mean(count_ls))
    print(f"Алгоритм '{predict_func.__name__}' угадывает число в среднем за: {score} попыток")
    return score


def compare_algorithms() -> None:
    """
    Сравнивает эффективность разных алгоритмов угадывания.
    """
    # Тестируем случайный алгоритм
    random_score = score_game(random_predict, fix_seed=True)
    # Тестируем алгоритм бинарного поиска
    binary_score = score_game(binary_search_predict, fix_seed=True)

    print("=" * 50)
    print(f"Бинарный поиск эффективнее случайного в {random_score / binary_score:.1f} раз")


if __name__ == "__main__":
    # Запуск сравнения алгоритмов
    compare_algorithms()
