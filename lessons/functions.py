"""Demonstrates functions"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    
print(my_max(66, 1))