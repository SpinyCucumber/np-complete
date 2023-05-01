def _find_subset(elements, goal, included):
    # Base cases
    if goal == 0:
        return included
    # "Elements sum" optimization
    if len(elements) == 0:
        return None
    # Recursive case
    remaining_elements = set(elements)
    removed = remaining_elements.pop()
    return _find_subset(remaining_elements, goal - removed, included | {removed}) or _find_subset(remaining_elements, goal, included)

def find_subset_exhaustive(elements: set[int], goal: int):
    """
    Brute-force recursive solution
    Terminates branch if sum of elements less than target
    """
    return _find_subset(elements, goal, frozenset())

def find_subset_fast(elements: set[int], goal: int) -> set[int]:
    # Sort elements
    deck = list(elements)
    hand = []
    hand_sum = 0
    previous_sums = {hand_sum}
    num_iters = 0

    def is_valid_weight(weight):
        return not (weight + hand_sum) in previous_sums

    # Iterate until solution found
    while hand_sum != goal:

        # Find element closest to requirement that doesn't produce sum previously seen
        # This is a memory-intensive algorithm
        diff = goal - hand_sum
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

    print(f'Iterations: {num_iters}')

    # Hand contains solution
    return set(hand)