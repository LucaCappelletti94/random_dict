"""Module to generate random dictionaries with different types of values."""

import sys
from typing import Callable, List, Tuple, Dict, Union, Optional, Any
from random import randint, uniform, getrandbits, choice, shuffle, Random
from string import ascii_uppercase, digits
from itertools import product


def random_int(
    random_state: Optional[Random] = None,
) -> int:
    """Return a random integer.

    Parameters
    ---------------------
    random_state: Optional[Random] = None,
        Random state to use.
        If None, the default random state is used.
    """
    if random_state is not None:
        return random_state.randint(-sys.maxsize, sys.maxsize)
    return randint(-sys.maxsize, sys.maxsize)


def random_float(random_state: Optional[Random] = None) -> float:
    """Return a random float.

    Parameters
    ---------------------
    random_state: Optional[Random] = None,
        Random state to use.
        If None, the default random state is used.
    """
    if random_state is not None:
        return random_state.uniform(-sys.maxsize, sys.maxsize)
    return uniform(-sys.maxsize, sys.maxsize)


def random_bool(
    random_state: Optional[Random] = None,
) -> bool:
    """Return a random boolean.

    Parameters
    ---------------------
    random_state: Optional[Random] = None,
        Random state to use.
        If None, the default random state is used.
    """
    if random_state is not None:
        return bool(random_state.getrandbits(1))
    return bool(getrandbits(1))


def random_string(
    random_state: Optional[Random] = None,
) -> str:
    """Return a random string.

    Parameters
    ---------------------
    random_state: Optional[Random] = None,
        Random state to use.
        If None, the default random state is used
    """
    if random_state is not None:
        return "".join(
            random_state.choice(ascii_uppercase + digits)
            for _ in range(random_state.randint(0, 1000))
        )
    return "".join(choice(ascii_uppercase + digits) for _ in range(randint(0, 1000)))


def random_bytes(
    random_state: Optional[Random] = None,
) -> bytes:
    """Return a random bytes sequence.

    Parameters
    ---------------------
    random_state: Optional[Random] = None,
        Random state to use.
        If None, the default random state is used.
    """
    return random_string(random_state=random_state).encode()


def random_tuple(
    random_state: Optional[Random] = None,
) -> Tuple:
    """Return a random tuple.

    Parameters
    ---------------------
    random_state: Optional[Random] = None,
        Random state to use.
        If None, the default random state is used.
    """
    generators = random_int, random_float, random_bool, random_string, random_bytes
    first = (
        random_state.choice(generators)
        if random_state is not None
        else choice(generators)
    )
    second = (
        random_state.choice(generators)
        if random_state is not None
        else choice(generators)
    )
    return first(random_state=random_state), second(random_state=random_state)


try:
    import pandas as pd  # pylint: disable=wrong-import-position

    def random_pandas_dataframe(
        random_state: Optional[Random] = None,
    ) -> pd.DataFrame:
        """Return a random dataframe.

        Parameters
        ---------------------
        random_state: Optional[Random] = None,
            Random state to use.
            If None, the default random state is used.
        """
        return pd.DataFrame(
            {
                random_string(random_state=random_state): random_tuple(
                    random_state=random_state
                ),
            }
        )

    def random_pandas_series(
        random_state: Optional[Random] = None,
    ) -> pd.Series:
        """Return a random series.

        Parameters
        ---------------------
        random_state: Optional[Random] = None,
            Random state to use.
            If None, the default random state is used.
        """
        return pd.Series(
            {
                random_string(random_state=random_state): random_tuple(
                    random_state=random_state
                ),
            }
        )

except ImportError:

    def random_pandas_dataframe(
        random_state: Optional[Random] = None,
    ) -> None:
        """Return a random dataframe."""
        raise ImportError("Pandas is not installed. Run `pip install pandas`.")

    def random_pandas_series(
        random_state: Optional[Random] = None,
    ) -> None:
        """Return a random series."""
        raise ImportError("Pandas is not installed. Run `pip install pandas`.")


try:
    import numpy as np  # pylint: disable=wrong-import-position

    def random_numpy_array(
        random_state: Optional[Random] = None,
    ) -> np.ndarray:
        """Return a short numpy array.

        Parameters
        ---------------------
        random_state: Optional[Random] = None,
            Random state to use.
            If None, the default random state is used.
        """
        return np.array(random_tuple(random_state=random_state))

except ImportError:

    def random_numpy_array(
        random_state: Optional[Random] = None,
    ) -> None:
        """Return a short numpy array."""
        raise ImportError("Numpy is not installed. Run `pip install numpy`.")


def _value_gen(
    sources: List[Callable], number: int, random_state: Optional[Random]
) -> Callable:
    for _ in range(number):
        if random_state is not None:
            yield random_state.choice(sources)
        else:
            yield choice(sources)


def random_string_dict(
    max_depth: int, max_height: int, random_state: Optional[Union[Random, int]] = None
) -> Dict[str, str]:
    """Return a random dictionary of string with at most given max_depth and max_height.

    Parameters
    ---------------------
    max_depth: int,
        Maximum depth of dictionary.
    max_height: int,
        Maximum height of dictionary.
    random_state: Optional[Union[Random, int]] = None,
        Random state to use.
        If None, the default random state is used.
    """
    return random_dict(
        max_depth=max_depth,
        max_height=max_height,
        key_generators=random_string,
        value_generators=random_string,
        random_state=random_state,
    )


def random_bool_dict(
    max_depth: int, max_height: int, random_state: Optional[Union[Random, int]] = None
) -> Dict[bool, bool]:
    """Return a random dictionary of bool with at most given max_depth and max_height.

    Parameters
    ---------------------
    max_depth: int,
        Maximum depth of dictionary.
    max_height: int,
        Maximum height of dictionary.
    random_state: Optional[Union[Random, int]] = None,
        Random state to use.
        If None, the default random state is used.
    """
    return random_dict(
        max_depth=max_depth,
        max_height=max_height,
        key_generators=random_bool,
        value_generators=random_bool,
        random_state=random_state,
    )


def random_float_dict(
    max_depth: int, max_height: int, random_state: Optional[Union[Random, int]] = None
) -> Dict[float, float]:
    """Return a random dictionary of floats with at most given max_depth and max_height.

    Parameters
    ---------------------
    max_depth: int,
        Maximum depth of dictionary.
    max_height: int,
        Maximum height of dictionary.
    random_state: Optional[Union[Random, int]] = None,
        Random state to use.
        If None, the default random state is used.
    """
    return random_dict(
        max_depth=max_depth,
        max_height=max_height,
        key_generators=random_float,
        value_generators=random_float,
        random_state=random_state,
    )


def random_int_dict(
    max_depth: int, max_height: int, random_state: Optional[Union[Random, int]] = None
) -> Dict[int, int]:
    """Return a random dictionary of integers with at most given max_depth and max_height.

    Parameters
    ---------------------
    max_depth: int,
        Maximum depth of dictionary.
    max_height: int,
        Maximum height of dictionary.
    random_state: Optional[Union[Random, int]] = None,
        Random state to use.
        If None, the default random state is used.
    """
    return random_dict(
        max_depth=max_depth,
        max_height=max_height,
        key_generators=random_int,
        value_generators=random_int,
        random_state=random_state,
    )


def all_generators() -> List[Callable]:
    """Return all available generators."""
    generators = [
        random_int,
        random_float,
        random_bool,
        random_string,
        random_bytes,
        random_tuple,
    ]
    try:
        import pandas  # pylint: disable=wrong-import-position,unused-import,import-outside-toplevel

        generators.extend([random_pandas_dataframe, random_pandas_series])
    except ImportError:
        pass

    try:
        import numpy  # pylint: disable=wrong-import-position,unused-import,import-outside-toplevel

        generators.append(random_numpy_array)
    except ImportError:
        pass

    return generators


def random_dict(
    max_depth: int,
    max_height: int,
    key_generators: Union[str, Tuple[Callable]] = "all",
    value_generators: Union[str, Tuple[Callable]] = "all",
    generators_combinations: int = 5,
    random_state: Optional[Union[Random, int]] = None,
) -> Dict[Any, Any]:
    """Return a random dictionary with at most given max_depth and max_height.

    Parameters
    ---------------------
    max_depth: int,
        Maximum depth of dictionary.
    max_height: int,
        Maximum height of dictionary.
    key_generators: Tuple[Callable],
        Functions used to populate the dictionary keys.
    value_generators: Tuple[Callable],
        Functions used to populate the dictionary values.
    generators_combinations: int = 5,
        Functions combinations to use.
    random_state: Optional[Union[Random, int]] = None,
        Random state to use.
        If None, the default random state is used.

    Returns
    ---------------------
    Random dictionary.
    """
    if isinstance(random_state, int):
        random_state = Random(random_state)

    if isinstance(key_generators, Callable):
        key_generators = (key_generators,)

    if isinstance(value_generators, Callable):
        value_generators = (value_generators,)

    if key_generators == "all":
        key_generators = [
            generator
            for generator in all_generators()
            if generator
            not in (
                random_pandas_dataframe,
                random_numpy_array,
                random_pandas_series,
            )
        ]

    if value_generators == "all":
        value_generators = all_generators()

    generators_tuples = list(
        product(
            _value_gen(key_generators, max_height, random_state=random_state),
            _value_gen(value_generators, max_height, random_state=random_state),
        )
    )

    if random_state is not None:
        random_state.shuffle(generators_tuples)
    else:
        shuffle(generators_tuples)

    return {
        key_gen(random_state=random_state): (
            random_dict(
                max_depth=(
                    randint(1, max_depth - 1)
                    if random_state is None
                    else random_state.randint(1, max_depth - 1)
                ),
                max_height=(
                    randint(1, max_height - 1)
                    if random_state is None
                    else random_state.randint(1, max_height - 1)
                ),
                key_generators=key_generators,
                value_generators=value_generators,
                random_state=random_state,
            )
            if max_depth > 1 and max_height > 1
            else val_gen(random_state=random_state)
        )
        for key_gen, val_gen in generators_tuples[:generators_combinations]
    }
