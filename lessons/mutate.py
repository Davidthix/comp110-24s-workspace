"""Mutating functions."""

__author__ = "730664354"

def manual_append(a: list[int],b: int) -> None:
    a.append(b)

def double(a: list[int]) -> None:
    list_idx: int = 0
    while list_idx <= len(a) -1:
        a[list_idx] *= 2
        list_idx += 1