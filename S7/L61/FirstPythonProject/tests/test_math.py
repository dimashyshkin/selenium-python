import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 2) == 30, "The sum of 1 and 2 should be 3"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "The sum of 100 and 300 should be 400"
