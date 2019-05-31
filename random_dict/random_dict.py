from random import randint, uniform, getrandbits, choice
from typing import Callable, List, Tuple, Dict
from string import ascii_uppercase, digits
import sys

def random_int()->int:
    """Return a random integer."""
    return randint(-sys.maxsize, sys.maxsize)

def random_float()->float:
    """Return a random float."""
    return uniform(-sys.maxsize, sys.maxsize)

def random_bool()->bool:
    """Return a random boolean."""
    return bool(getrandbits(1))

def random_string()->str:
    """Return a random string."""
    return ''.join(choice(ascii_uppercase + digits) for _ in range(randint(0, 1000)))

def _value_gen(sources:List[Callable], number:int)->Callable:
    for _ in range(number):
        yield choice(sources)

def random_string_dict(max_depth:int, max_height:int)->Dict:
    """Return a random dictionary of string with at most given max_depth and max_height.
        max_depth:int, maximum depth of dictionary.
        max_height:int, maximum height of dictionary.
    """
    return random_dict(max_depth, max_height, (random_string,))

def random_bool_dict(max_depth:int, max_height:int)->Dict:
    """Return a random dictionary of bool with at most given max_depth and max_height.
        max_depth:int, maximum depth of dictionary.
        max_height:int, maximum height of dictionary.
    """
    return random_dict(max_depth, max_height, (random_bool,))

def random_float_dict(max_depth:int, max_height:int)->Dict:
    """Return a random dictionary of floats with at most given max_depth and max_height.
        max_depth:int, maximum depth of dictionary.
        max_height:int, maximum height of dictionary.
    """
    return random_dict(max_depth, max_height, (random_float,))

def random_int_dict(max_depth:int, max_height:int)->Dict:
    """Return a random dictionary of integers with at most given max_depth and max_height.
        max_depth:int, maximum depth of dictionary.
        max_height:int, maximum height of dictionary.
    """
    return random_dict(max_depth, max_height, (random_int,))

def random_dict(max_depth:int, max_height:int, generators:Tuple[Callable]=(random_int, random_bool, random_float, random_string))->Dict:
    """Return a random dictionary with at most given max_depth and max_height.
        max_depth:int, maximum depth of dictionary.
        max_height:int, maximum height of dictionary.
        generators:Tuple[Callable], functions used to populate the dictionary.
    """
    assert max_depth>0
    assert max_height>0
    return {
        key_gen():random_dict(randint(1, max_depth-1), randint(1, max_height-1), generators) if max_depth>1 and max_height>1 else val_gen()
        for key_gen, val_gen in zip(_value_gen(generators, max_height), _value_gen(generators, max_height))
    }