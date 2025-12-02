#!/usr/bin/python
import numpy as np
import pandas as pd
from pandas import DataFrame


def gen_array_with_linspace(
    _start, _stop, _num=50, _endpoint=True, _retstep=True, _dtype=None
):
    # Генерируем массив из 60 чисел от -6 до 21 включительно
    array, step = np.linspace(
        start=_start,
        stop=_stop,
        num=_num,
        endpoint=_endpoint,
        retstep=_retstep,
        dtype=_dtype,
    )

    # Выведем первые несколько элементов для наглядности
    print("Первые 5 элементов:")
    print(array[:5])
    # print(f"Шаг между элементами: {round(array[1] - array[0], 2)}")
    print(f"Шаг между элементами: {round(step, 2)}")


def min_max_dist(*vectors):
    vectors = np.array(vectors)
    n = len(vectors)

    # Создаем матрицу всех попарных расстояний
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(vectors[i] - vectors[j])

    # Создаем маску для верхнего треугольника (без диагонали)
    mask = np.triu(np.ones((n, n), dtype=bool), k=1)
    distances = dist_matrix[mask]

    return np.min(distances), np.max(distances)


def create_company_df(income, expenses, years) -> DataFrame:
    df = pd.DataFrame(
        data={
            "Income": income,
            "Expenses": expenses,
        },
        index=years,
    )
    return df


if __name__ == "__main__":
    gen_array_with_linspace(_start=-6, _stop=21, _num=60)
    gen_array_with_linspace(_start=-6, _stop=21, _num=60, _endpoint=False)
