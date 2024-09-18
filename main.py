from binary_search_approach import binary_search_approach
from math_approach import math_approach


def main():
    n = 100000
    first_missing = 8345
    second_missing = 90212
    sequence = [x for x in range(1, n + 1) if x not in (first_missing, second_missing)]

    print(math_approach(sequence, n))  # Time complexity = O(n)
    print(binary_search_approach(sequence, n))  # Time complexity = O(log(n))


if __name__ == '__main__':
    main()
