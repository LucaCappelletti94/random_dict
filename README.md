# random_dict

[![pip](https://badge.fury.io/py/random-dict.svg)](https://badge.fury.io/py/random-dict)
[![downloads](https://pepy.tech/badge/random-dict)](https://pepy.tech/projects/random-dict)
[![license](https://img.shields.io/github/license/rafaeltoledo/random_dict)](LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/random-dict)](https://pypi.org/project/random-dict/)
[![GitHub actions](https://github.com/LucaCappelletti94/random_dict/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/random_dict/actions/)

Python package to generate random dictionaries of given types.

It is primarily intended for testing/fuzzing purposes, where you need to generate many random dictionaries of a given type.

## How do I install this package?
As usual, just download it using pip:

```shell
pip install random_dict
```

## Usage examples
Here are some examples of how to use this package.

### Generator random_string_dict

This function will generate a dictionary with given at most `max_depth` and `max_height` of type `string`.

```python
from random_dict import random_string_dict
from random import randint

random_string_dict(
    max_depth=randint(1, 10),
    max_height=randint(1, 10)
)
```

### Generator random_bool_dict

This function will generate a dictionary with given at most `max_depth` and `max_height` of type `bool`.

```python
from random_dict import random_bool_dict
from random import randint

random_bool_dict(
    max_depth=randint(1, 10),
    max_height=randint(1, 10)
)
```

### Generator random_float_dict

This function will generate a dictionary with given at most `max_depth` and `max_height` of type `float`.

```python
from random_dict import random_float_dict
from random import randint

random_float_dict(
    max_depth=randint(1, 10),
    max_height=randint(1, 10)
)
```

### Generator random_int_dict

This function will generate a dictionary with given at most `max_depth` and `max_height` of type `int`.

```python
from random_dict import random_int_dict
from random import randint

random_int_dict(
    max_depth=randint(1, 10),
    max_height=randint(1, 10)
)
```

### Generator random_dict

This function will generate a dictionary with given at most `max_depth` and `max_height` of mixed types.

```python
from random_dict import random_dict
from random import randint

random_dict(
    max_depth=randint(1, 10),
    max_height=randint(1, 10)
)
```

Some generated examples can be found within the examples folder.

## License
This project is licensed under the terms of the MIT license.
