from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas


def test_version():
    assert __version__ == '0.1.0'


def test_fib():
    outputs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for i in range(len(outputs)):
        assert outputs[i] == fibonacci(i)


def test_lucas():
    outputs = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]
    for i in range(len(outputs)):
        assert outputs[i] == lucas(i)

