"""Writing methods with different return types."""

from __future__ import annotations

__author__ = "730664354"


class Point:
    """A point with coordinates."""

    x: float
    y: float

    def __init__(self, x_input: float, y_input: float):
        """Creates a point with certain x and y values."""
        self.x = x_input
        self.y = y_input

    def scale_by(self, factor: int) -> None:
        """Multiplies the x and y coordinates by a certain factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new Point object with x and y values of the previous Point multiplies by a certain factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point