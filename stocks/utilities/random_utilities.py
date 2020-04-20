import random
import string


def random_string(size=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def random_letters(size=8):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(size))


def random_letters_lowercase(size=8):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def random_int(min=0, max=100):
    return random.randint(min, max)


def random_double(min=0, max=100, precision=2):
    unrounded = random.uniform(min, max)
    rounded = round(unrounded, precision)
    return rounded
