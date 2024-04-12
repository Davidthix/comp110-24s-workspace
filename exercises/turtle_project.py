"""Working with recursion and drawing with Turtle objects."""

__author__ = "730664354"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Sets up the scene."""
    leo: Turtle = Turtle()
    draw_animal(leo, 50, -100, "blue")
    draw_tree(leo, 150, -100, 0)
    draw_tree(leo, 200, -100, 0)
    draw_target(leo, -200, -50, 0)
    draw_arrow(leo, -100, -100)
    done()


def draw_rectangle(turtle: Turtle, color: str, bottom_side_length: float, side_side_length: float) -> None:
    """Draws a rectangle."""
    turtle.color(color)
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(bottom_side_length)
        turtle.right(90)
        turtle.forward(side_side_length)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def go_to_location(turtle: Turtle, x: float, y: float) -> None:
    """Moves turtle to a coordinate pair."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def turn_left_and_move(turtle: Turtle, distance: float) -> None:
    """Turns turtle 90 degrees left and move it a certain distance."""
    turtle.left(90)
    turtle.forward(distance)


def turn_right_and_move(turtle: Turtle, distance: float) -> None:
    """Turns turtle 90 degrees right and move it a certain distance."""
    turtle.right(90)
    turtle.forward(distance)


def draw_equilateral_triangle(turtle: Turtle, color: str, side_length: float) -> None:
    """Draws an equilateral triangle."""
    turtle.color(color)
    turtle.begin_fill()
    i: int = 0
    while i < 3:
        turtle.forward(side_length)
        turtle.left(120)
        i += 1
    turtle.end_fill()


def draw_tree(turtle: Turtle, x: float, y: float, start_angle: int) -> None:
    """Draws a tree."""
    go_to_location(turtle, x, y)
    turtle.seth(start_angle)
    draw_rectangle(turtle, "brown", 25, 50)
    turtle.penup()
    turtle.backward(25)
    turtle.pendown()
    side_length: float = 75
    while side_length > 50:
        draw_equilateral_triangle(turtle, "green", side_length)
        turtle.penup()
        turn_left_and_move(turtle, side_length / 6)
        turn_right_and_move(turtle, (side_length - (side_length * .95)) / 2)
        turtle.pendown()
        side_length *= .95


def draw_target(turtle: Turtle, x: int, y: int, start_angle: int) -> None:
    """Draws a square target."""
    go_to_location(turtle, x, y)
    turtle.seth(start_angle)
    i: int = 0
    side_length: int = 50
    while i < 6:
        if i % 2 == 0:
            draw_rectangle(turtle, "red", side_length, side_length)
        else: 
            draw_rectangle(turtle, "white", side_length, side_length)
        turtle.penup()
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.left(90)
        turtle.pendown()
        side_length -= 8
        i += 1


def draw_arrow(turtle: Turtle, x: int, y: int) -> None:
    """Draws an arrow."""
    go_to_location(turtle, x, y)
    turtle.seth(90)
    side_length: float = 15
    draw_equilateral_triangle(turtle, "grey", side_length)
    turtle.forward(side_length * (2 / 3))
    turtle.right(90)
    draw_rectangle(turtle, "brown", 40, side_length * (1 / 3))
    turtle.forward(40)


def draw_animal(turtle: Turtle, x: int, y: int, color: str) -> None:
    """Draws an animal."""
    go_to_location(turtle, x, y)
    turtle.color(color)
    turtle.seth(0)
    i: int = 0
    while i < 4:
        draw_rectangle(turtle, color, 10, 30)
        if i % 2 == 0:
            turtle.forward(12)
        elif not i > 1:
            turtle.forward(30)
        i += 1
    turtle.backward(54)
    turn_left_and_move(turtle, 20)
    turtle.right(90)
    draw_rectangle(turtle, color, 64, 20)
    turn_right_and_move(turtle, 15)
    turn_left_and_move(turtle, -30)
    turn_left_and_move(turtle, 30)
    turtle.right(90)
    draw_rectangle(turtle, color, 30, 30)
    draw_equilateral_triangle(turtle, "black", 10)
    turtle.forward(20)
    draw_equilateral_triangle(turtle, "black", 10)


if __name__ == "__main__":
    main()