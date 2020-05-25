import datetime
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


def random_date(start_year=2000):
    current_date = datetime.datetime.now().date()
    start_date = datetime.datetime(start_year, 1, 1).date()
    delta = current_date - start_date
    random_days = random_int(0, delta.days)
    add_days = start_date + datetime.timedelta(days=random_days)
    return add_days
