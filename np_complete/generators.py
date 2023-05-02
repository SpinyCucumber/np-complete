from random import randrange
from .definitions import SubsetSum

def generate_subset_sum(high: int, n: int, target: int):
    """
    Generates an instance of the subset sum problem with a given target sum and n integers uniformly distributed from the range [0, high)
    """
    return SubsetSum(target, [randrange(0, high) for i in range(n)])

__all__ = ["generate_subset_sum"]