"""Second battleship program."""

__author__ = "730664354"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row: int = int(input("Guess a row: "))
while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_column: int = int(input("Guess a column: "))
while guess_column > grid_size or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
results_box: str = ""
if guess_row == secret_row and guess_column == secret_column:
    results_box = RED_BOX
else:
    results_box = WHITE_BOX

row_idx: int = 1

while row_idx <= grid_size:
    row_print: str = ""
    column_idx: int = 1
    if guess_row == row_idx:
        while column_idx <= grid_size:
            if guess_column == column_idx:
                row_print += results_box
            else:
                row_print += BLUE_BOX
            column_idx += 1
    else:
        while column_idx <= grid_size:
            row_print += BLUE_BOX
            column_idx += 1
    print(row_print)
    row_idx += 1


if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")