from typing import List
from sympy.logic import And
from dataclasses import dataclass

@dataclass
class SubsetSum:
    """
    An instance of the subset sum problem
    Contains a target sum and a list of positive integers
    """
    target: int
    numbers: List[int]

@dataclass
class Partition:
    """
    An instance of the partition problem
    Contains a list of positive integers
    """
    numbers: List[int]

@dataclass
class Sat:
    """
    An instance of the boolean satisfiability problem
    Contains a boolean expression in CNF form (the top-level expression is And)
    """
    expression: And

__all__ = ["SubsetSum", "Partition", "Sat"]