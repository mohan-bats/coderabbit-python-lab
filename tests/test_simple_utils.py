from simple_utils import (
    reverse_string,
    count_words,
    celsius_to_fahrenheit,
)


def test_reverse_string():
    assert reverse_string("rabbit") == "tibbar"


def test_count_words():
    assert count_words("hello little rabbit") == 3


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212