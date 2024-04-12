"Turtle tutorial."

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()
colormode(255)

i: int = 0
leo.color("red")
leo.begin_fill()
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


h: int = 0
bob.color("black")
bob.speed(11)
side_length: int = 300
while h < 200:
    j: int = 0
    while j < 3:
        bob.forward(side_length)
        bob.left(120)
        j += 1
    h += 1
    side_length *= .95
done()