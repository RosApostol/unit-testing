import pytest
import math

from src.main import *


def test_add_simple():
    a, b = 5, 3
    actual_result = add(a, b)
    expected_result = 8
    assert expected_result == actual_result


def test_complex_data_types_1():
    expected = [1, 2, 3]
    actual = [1, 2, 3]
    assert actual == expected


def test_complex_data_types_2():
    expected = [1, 2, 3]
    actual = 1
    assert actual in expected


def test_before_after(setup_and_teardown):
    result = setup_and_teardown
    assert result == "Hello World"


@pytest.mark.parametrize("a,b,expected",
                         [
                             (3, 5, 8),
                             (2.2, 1.1, 3.3),
                             (0, 0.0, 0),
                             (-2, -3.2, -5.2)
                         ]
                         )
def test_add(a, b, expected):
    actual_result = add(a, b)
    # assert expected == actual_result
    assert math.isclose(actual_result, expected)


def test_approx():
    assert 3.14 == pytest.approx(3.14159, rel=0.01)


def test_assertion_msg():
    assert 10 == 9, "Something is NOT OK"


def test_divide_by_zero():
    a = 1
    b = 0

    with pytest.raises(ZeroDivisionError):
        divide(a, b)


def test_return_fine_df(my_test_df):  # taking my_test_df from conftest.py without importing it
    fine_df = return_fine_df()
    assert fine_df.equals(my_test_df)


# --- MARKING CAPABILITIES ---

@pytest.mark.my_own_mark
def test_1():
    assert True


@pytest.mark.my_own_mark
def test_2():
    assert True
