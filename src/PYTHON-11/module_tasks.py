#!/usr/bin/python
import pandas as pd
from pandas import DataFrame
from typing import Tuple

countries_df = pd.DataFrame(
    {
        "country": [
            "Англия",
            "Канада",
            "США",
            "Россия",
            "Украина",
            "Беларусь",
            "Казахстан",
        ],
        "population": [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
        "area": [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902],
    }
)


def calculate_density(df) -> Tuple[DataFrame, float]:
    """Добавляет в DataFrame столбец с плотностью населения.
    Добавляет в DataFrame столбец с булевыми значениями,
    обозначающими, что плотность населения выше среднего
    Returns: DataFrame с добавленными столбцами, mean_density
    """
    df["population_density"] = df["population"] * 1_000_000 / df["area"]
    mean_density = df["population_density"].mean()
    df["above_average_density"] = df["population_density"] > mean_density
    return df, mean_density


def get_experience(arg):
    """
    Преобразует строку с опытом работы в количество месяцев.
    Args:
        arg (str): Строка с опытом работы в формате
                   "X лет Y мес" или "X лет" или "Y мес"
    Returns:
        int: Количество месяцев опыта работы
    """
    words = arg.split()
    months = 0

    # Проверяем месяцы (если они есть в конце)
    if words and words[-1].startswith("мес"):
        months += int(words[-2])
        words = words[:-2]

    # Проверяем годы
    if words and (words[-1].startswith("лет") or words[-1].startswith("год")):
        months += 12 * int(words[-2])

    return months


# Функции для проверки наличия столбцов в DataFrame
def check_all_columns_fast(df, columns):
    """Проверяет, что все указанные столбцы существуют"""
    existing = set(df.columns)
    return all(col in existing for col in columns)


def check_any_column_fast(df, columns):
    """Проверяет, существует ли хотя бы один из столбцов"""
    existing = set(df.columns)
    return any(col in existing for col in columns)


def get_existing_missing_fast(df, columns):
    """Возвращает кортеж (существующие, отсутствующие) столбцы"""
    existing = set(df.columns)
    existing_cols = [col for col in columns if col in existing]
    missing_cols = [col for col in columns if col not in existing]
    return existing_cols, missing_cols


if __name__ == "__main__":
    countries_df, mean_population_density = calculate_density(countries_df)
    print(round(mean_population_density, 2))
    print(countries_df)

    required = [
        "population_density",
        "above_average_density",
    ]
    print(f"столбцы существуют: {check_all_columns_fast(countries_df, required)}")

    data = {
        "Опыт работы": [
            "Опыт работы 8 лет 3 месяца",
            "Опыт работы 3 года 5 месяцев",
            "Опыт работы 1 год 9 месяцев",
            "Опыт работы 3 месяца",
            "Опыт работы 6 лет",
        ]
    }
    df = pd.DataFrame(data)
    # Применяем функцию к столбцу
    df["Опыт в месяцах"] = df["Опыт работы"].apply(get_experience)
    print("Исходные данные:")
    print(df[["Опыт работы"]].to_string(index=False))
    print("\nРезультат преобразования:")
    print(df["Опыт в месяцах"].to_string(index=False))
    pass
