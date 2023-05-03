from .definitions import SubsetSum

def find_subset_exhaustive(subset_sum: SubsetSum) -> set[int]:
    """
    Subset Sum Brute-force Search

    Uses a recursive, exponential-time algorithm to search the entire problem space.
    """

    def find_subset(index: int, target: int, included: set[int]):
        if target == 0:
            return included
        if target < 0 or index == len(subset_sum.numbers):
            return None
        # Recursive case
        num = subset_sum.numbers[index]
        return find_subset(index + 1, target - num, included | {num}) or find_subset(index + 1, target, included)

    return find_subset(0, subset_sum.target, frozenset())

def find_subset_optimized(subset_sum: SubsetSum) -> set[int]:
    """
    Subset Sum Brute-force Search (Optimized)

    Uses a recursive, exponential-time algorithm to search the entire problem space.
    For each recursive branch, if the target sum is greater than the total sum or less than 0, we terminate the branch.
    If the target sum is 0 or equal to the total sum, we have found a solution
    """

    # len(cumulative_sum) = len(numbers) + 1
    # Final element is total sum
    s = 0
    cumulative_sum = []
    for num in subset_sum.numbers:
        cumulative_sum.append(s)
        s += num
    cumulative_sum.append(s)

    def find_subset(index: int, target: int, included: set[int]):
        # We calculate the total sum of the numbers in the set
        # Note that the set is determined by slicing the original set
        high = cumulative_sum[-1] - cumulative_sum[index]
        # Base cases
        if target > high:
            return None
        if target == high:
            return included | set(subset_sum.numbers[index:])
        if target < 0:
            return None
        if target == 0:
            return included
        # Recursive case
        num = subset_sum.numbers[index]
        return find_subset(index + 1, target - num, included | {num}) or find_subset(index + 1, target, included)

    return find_subset(0, subset_sum.target, frozenset())

def find_subset_greedy(subset_sum: SubsetSum) -> set[int]:
    subset_sum_sorted = SubsetSum(subset_sum.target, sorted(subset_sum.numbers, reverse=True))
    return find_subset_optimized(subset_sum_sorted)

__all__ = ["find_subset_exhaustive", "find_subset_optimized", "find_subset_greedy"]