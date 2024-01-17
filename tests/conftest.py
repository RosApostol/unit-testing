import pytest
import pandas as pd


@pytest.fixture
def my_test_df():
    return pd.DataFrame({
        "A": [1, 2],
        "B": [3, 4]
    })


@pytest.fixture
def setup_and_teardown():
    print("Something happens BEFORE test ...")

    yield "Hello World!"

    print("Something happens AFTER the test ...")

