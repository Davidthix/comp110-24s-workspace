"""Using recursion to return the product of two variables."""

__author__ = "730664354"


def f(n: int, k: int) -> int:
    """Returns the product of n and k using recursion."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)