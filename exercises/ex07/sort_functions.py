"""Functions that implement sorting algorithms."""


__author__ = "730664354"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.

    Insert into an already sorted list.
    """
    sorted_idx: int = 0
    unsorted_value: int = 0
    for list_idx in range(0, len(x)):
        unsorted_value = x[list_idx]
        sorted_idx = list_idx - 1
        while sorted_idx >= 0:
            if unsorted_value < x[sorted_idx]:
                temp_unsorted_idx_value: int = x[sorted_idx]
                x[sorted_idx] = unsorted_value
                x[sorted_idx + 1] = temp_unsorted_idx_value
            sorted_idx -= 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm.

    Repeatedly find the minimum and swap it.
    """
    idx: int = 0
    for value_idx in range(0, len(x) - 1):
        min_value_idx = idx + 1
        min_value: int = x[min_value_idx]
        for value_idx_2 in range(idx + 1, len(x)):
            if x[value_idx_2] < min_value:
                min_value_idx = value_idx_2
                min_value = x[value_idx_2]
        if min_value < x[value_idx]:
            temp_int: int = x[value_idx]
            x[value_idx] = min_value
            x[min_value_idx] = temp_int
        idx += 1
    return None