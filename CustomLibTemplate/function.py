import numpy as np
from typing import List

__all__ = ['random_array']


def random_array(size: List[int]) -> np.ndarray:
    """
    Initial random array

    Args:
        size (List[int]): shape of array

    Returns:
        str: Concatenated string
    """
    return np.random.rand(*size)