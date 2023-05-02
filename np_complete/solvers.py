from .definitions import SubsetSum

def find_subset_exhaustive(subset_sum: SubsetSum) -> set[int]:
    """
    Subset Sum Brute-force Search

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

    def _find_subset(index: int, target: int, included: set[int]):
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
        return _find_subset(index + 1, target - num, included | {num}) or _find_subset(index + 1, target, included)

    return _find_subset(0, subset_sum.target, frozenset())

def find_subset_fast(subset_sum: SubsetSum) -> set[int]:

    # Sort elements
    deck = list(subset_sum.numbers)
    hand = []
    hand_sum = 0
    previous_sums = {hand_sum}
    num_iters = 0

    def is_valid_weight(weight):
        return not (weight + hand_sum) in previous_sums

    # Iterate until solution found
    while hand_sum != subset_sum.target:

        # Find element closest to requirement that doesn't produce sum previously seen
        # This is a memory-intensive algorithm
        diff = subset_sum.target - hand_sum
        weights = filter(lambda pair: is_valid_weight(pair[1]), enumerate([-elem for elem in hand] + deck))
        residuals = [(index, abs(weight - diff)) for index, weight in weights]
        # If no possible elements to move, all sums exhausted
        if len(residuals) == 0: return None

        min_index = min(residuals, key=lambda pair: pair[1])[0]
        if min_index >= len(hand):
            moved = deck.pop(min_index - len(hand))
            hand_sum += moved
            hand.append(moved)
        else:
            moved = hand.pop(min_index)
            hand_sum -= moved
            deck.append(moved)

        # Record sum
        print(moved)
        previous_sums.add(hand_sum)
        num_iters += 1

    # Hand contains solution
    return set(hand)

__all__ = ["find_subset_exhaustive", "find_subset_fast"]