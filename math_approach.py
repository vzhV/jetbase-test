def math_approach(sequence, n):
    # 1. Find the sum and sum of squares of the provided sequence
    # Time complexity = O(n). Because it's a linear number of operations
    sequence_sum = sum(sequence)
    sequence_sum_square = sum(x * x for x in sequence)

    # 1) Find the full sum and sum of squares of the sequence 1 to n via formulas
    # 2) Find the missing sum and sum of squares by subtracting the sequence values from the full values
    # 3) Solve the square equation via discriminant formula
    # Time complexity = O(1). Because it's a constant number of operations
    full_sum = n * (n + 1) // 2
    full_sum_squares = n * (n + 1) * (2 * n + 1) // 6

    sum_missing = full_sum - sequence_sum
    sum_squares_missing = full_sum_squares - sequence_sum_square

    xy = (sum_missing * sum_missing - sum_squares_missing) // 2
    discriminant = sum_missing * sum_missing - 4 * xy
    x = (sum_missing + discriminant ** 0.5) // 2
    y = sum_missing - x

    return int(x), int(y)
