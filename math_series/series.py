def sum_series(n, zero_val = 0, first_val = 1):
    if n == 0:
        return zero_val
    if n == 1:
        return first_val

    return sum_series(n - 1, zero_val, first_val) + sum_series(n - 2, zero_val, first_val)


def fibonacci(n):
    return sum_series(n)


def lucas(n):
    return sum_series(n, 2, 1)
