def binary_search_approach(sequence, n):
    # 1) Find the first missing number via binary search. Time complexity = O(log(n))
    first_missing = _binary_search(sequence, 0, n - 3, 1)

    # 2) Find the second missing number via binary search. Time complexity = O(log(n))
    second_missing = _binary_search(sequence, first_missing - 1, n - 3, 2)
    return first_missing, second_missing


def _binary_search(sequence, left, right, shift):
    # left - the left index of the search range
    # right - the right index of the search range
    # shift - how many numbers are missing before the current index
    while left <= right:
        mid = (left + right) // 2
        expected_value = mid + shift
        if sequence[mid] > expected_value:
            right = mid - 1
        else:
            left = mid + 1

    return left + shift
