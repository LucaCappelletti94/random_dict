from random_dict import random_bool_dict, random_float_dict, random_int_dict, random_string_dict, random_dict
from random import randint
import os
import json

def test_random_dict():
    for g in (random_bool_dict, random_float_dict, random_int_dict, random_string_dict, random_dict):
        with open("{f}.json".format(f=g.__name__), "w") as f:
            json.dump(g(randint(1, 10), randint(1, 10)), f, indent=4)
        os.remove("{f}.json".format(f=g.__name__))