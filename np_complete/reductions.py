# CS 470 Spring 2023, The University of Alabama
# Elijah Hilty

from sympy.logic import true, false, And, to_cnf
from sympy import symbols
from .definitions import SubsetSum, Sat, Partition

def half_adder(a, b):
    """
    Constructs a half-adder from 2 boolean expressions
    """
    return (a ^ b, a & b)

def full_adder(a, b, c):
    """
    Constructs a full-adder from 3 boolean expressions
    """
    s0, c0 = half_adder(a, b)
    s1, c1 = half_adder(s0, c)
    return (s1, c0 | c1)

def ripple_adder(A, B):
    """
    Constructs a ripple-carry adder which adds together two binary numbers

    a and b are arrays of boolean expressions and must have same length

    Produces an array of boolean expressions of the same length which is the sum
    """
    assert len(A) == len(B)
    c = false # Input to carry of next full adder
    S = [] # Sum bits
    for i in range(len(A)):
        s, c = full_adder(A[i], B[i], c)
        S.append(s)
    return S

def to_binary(n: int, num_bits: int):
    """
    Converts a number into an array of boolean values, which is its binary representation
    """
    result = []
    for i in range(num_bits):
        result.append(true if n % 2 else false)
        n = n // 2
    return result

def reduce_subset_sum_sat(subset_sum: SubsetSum, num_bits: int) -> Sat:
    """
    Converts an instance of the subset sum problem to an equisatisfiable SAT problem.
    That is, a solution to the input problem only if a the produced problem is satisfiable.

    This works by constructing an addition circuit equivalent to the subset sum problem.
    """
    # For each number in the set, we create an "enable bit."
    # These enable inputs are the variables in our SAT problem. The number is only
    # included in the subset of its enable bit is 1.
    n = len(subset_sum.numbers)
    enable = symbols(f"en:{n}")
    # We construct an adder chain, where the input to each adder is either 0 or a number
    # in the set, depending on the enable bit.
    S = [false for i in range(num_bits)]
    for i in range(n):
        A = [a & enable[i] for a in to_binary(subset_sum.numbers[i], num_bits)]
        S = ripple_adder(A, S)
    # We compare the final output to the target sum, producing the final expression
    # Comparison is performed using inverted XOR
    # We also convert to simplified CNF
    T = to_binary(subset_sum.target, num_bits)
    expression = And(*[~(S[i] ^ T[i]) for i in range(num_bits)])
    return Sat(to_cnf(expression))

def reduce_partition_subset_sum(partition: Partition) -> SubsetSum:
    """
    Converts an instance of the partition problem to an equisatisfiable subset sum problem.
    That is, a solution to the input problem only if a the produced problem is satisfiable.

    This is a very simple reduction which only requires summing the set if numbers and
    checking if a subset sums to half the total sum. Consequently, if the total sum is odd, no solution exists.
    """
    s = sum(partition.numbers)
    return SubsetSum(s/2, partition.numbers)

__all__ = ["reduce_subset_sum_sat", "reduce_partition_subset_sum"]