from random_dict import random_bool_dict, random_float_dict, random_int_dict, random_string_dict, random_dict
from random import randint
import os


def test_random_dict():
    for _ in range(100):
        for g in (random_bool_dict, random_float_dict, random_int_dict, random_string_dict, random_dict):
            g(randint(1, 10), randint(1, 10))
