"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730664354"

boat_location: int = int(input("Pick a secret boat location between 1 and 4: "))

if boat_location < 1:
    print("Error! " + str(boat_location) + " too low!")
    exit()
elif boat_location > 4:
    print("Error! " + str(boat_location) + " too high!")
    exit()

location_guess: int = int(input("Guess a number between 1 and 4: "))

if location_guess < 1:
    print("Error! " + str(location_guess) + " too low!")
    exit()
elif location_guess > 4:
    print("Error! " + str(location_guess) + " too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result: str = ""
display: str = ""

if location_guess == boat_location:
    result = RED_BOX
    if location_guess == 1:
        display = display + result
    else:
        display = display + BLUE_BOX
    if location_guess == 2:
        display = display + result
    else:
        display = display + BLUE_BOX
    if location_guess == 3:
        display = display + result
    else:
        display = display + BLUE_BOX
    if location_guess == 4:
        display = display + result
    else:
        display = display + BLUE_BOX
        print(display)
        print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    if location_guess == 1:
        display = display + result
    else:
        display = display + BLUE_BOX
    if location_guess == 2:
        display = display + result
    else:
        display = display + BLUE_BOX
    if location_guess == 3:
        display = display + result
    else:
        display = display + BLUE_BOX
    if location_guess == 4:
        display = display + result
    else:
        display = display + BLUE_BOX
        print(display)
        print("Incorrect! You missed the ship.")
