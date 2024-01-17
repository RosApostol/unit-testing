import pandas as pd


def say_hi(name):
    return f"Hello {name}!"


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def return_fine_df():
    # logic goes here
    return pd.DataFrame({
        "A": [1, 2],
        "B": [3, 4]
    })


def return_bad_df():
    # logic goes here
    return pd.DataFrame({
        "A": [1, 3],
        "B": [3, 4]
    })
