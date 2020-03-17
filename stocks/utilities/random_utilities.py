import random
import string


def random_string(size=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def random_letters(size=8):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(size))
