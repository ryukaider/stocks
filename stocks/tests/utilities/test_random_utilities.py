import os
import string
from utilities import random_utilities

root_path = os.path.join(os.path.dirname(__file__), '..', '..')


def test_random_string():
    assert random_utilities.random_string() is not None


def test_random_string_valid():
    random_string = random_utilities.random_string()
    for letter in random_string:
        assert letter in (string.ascii_letters + string.digits)


def test_random_string_length():
    length = 5
    random_string = random_utilities.random_string(length)
    assert len(random_string) == length


def test_random_letters():
    assert random_utilities.random_letters() is not None


def test_random_letters_valid():
    random_letters = random_utilities.random_letters()
    for letter in random_letters:
        assert letter in string.ascii_letters


def test_random_letters_length():
    length = 1
    random_letters = random_utilities.random_letters(length)
    assert len(random_letters) == length


def test_random_letters_lowercase():
    assert random_utilities.random_letters_lowercase() is not None


def test_random_letters_lowercase_valid():
    random_letters = random_utilities.random_letters_lowercase()
    for letter in random_letters:
        assert letter in string.ascii_lowercase


def test_random_letters_lowercase_length():
    length = 15
    random_letters = random_utilities.random_letters_lowercase(length)
    assert len(random_letters) == length
