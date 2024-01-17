from src.sample_class import SampleClass


def test_task_1():
    # pre-requisite
    sc = SampleClass(a=1, b=1)
    sc.task_1()

    # test
    actual_result = sc.a
    expected_result = 2

    assert expected_result == actual_result


def test_task_4():
    # pre-requisites
    sc = SampleClass(a=1, b=1)
    sc.c = 3  # this is expected for task 4; normally, task 3 should set this value

    # test
    actual_result = sc.task_4()
    expected_result = 5

    assert actual_result == expected_result
