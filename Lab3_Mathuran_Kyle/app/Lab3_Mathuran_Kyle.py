"""
Name: Mathuran Chandramohan, Kyle Angeles
Course: INFT 1207
Date: June 19th, 2025
Description: Set of functions that calculate the areas of a circle, trapezium, ellipse, and rhombus
"""

#region IMPORTS
from math import pi
#endregion IMPORTS

#region FUNCTIONS
def circle_area(radius):
    """Calculates area of circle given radius"""
    # checks for numeric input
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be int or float")

    # checks if numeric input is greater than 0
    if radius < 0:
        raise ValueError("Radius must be positive value")

    return pi*(radius**2)

def trapezium_area(base1, base2, height):
    """Calculates area of the trapezium given two numbers"""
    # checks for numeric input
    if type(base1) not in [int, float] and type(base2) not in [int, float]:
        raise TypeError("Base 1 and Base 2 must be int or float")
    if type (base1) not in [int, float]:
        raise TypeError("Base 1 must be int or float")
    if type (base2) not in [int, float]:
        raise TypeError("Base 2 must be int or float")
    if type(height) not in [int, float]:
        raise TypeError("Height must be must be int of float")

    #checks input for positive values
    if base1 <= 0 or base2 <= 0 or height <=0:
        raise ValueError("All values must be positive")

    #Calculates trapezium and returns area
    return 0.5 * (base1 + base2) * height

def ellipse_area(major_axis, minor_axis):
    """Calculates area of eclipse given major and minor axes"""
    # checks for numeric inputs
    if type(major_axis) not in [int, float] and type(minor_axis)not in [int, float]:
        raise TypeError("The major and minor axes must be in or float")
    if type(major_axis) not in [int, float]:
        raise TypeError("The major axis must be int or float")
    if type(minor_axis) not in [int, float]:
        raise TypeError("The minor axis must be int or float")

    # checks if numeric inputs is greater than 0
    if major_axis < 0 and minor_axis < 0:
        raise ValueError("Major and minor axes must be positive")
    if major_axis < 0:
        raise ValueError("Major axis must be positive")
    if minor_axis < 0:
        raise ValueError("Minor axis must be positive")

    return pi*major_axis*minor_axis

def rhombus_area(first_diagonal, second_diagonal):
    """Calculates the area of the rhombus given two diagonal input """
    # checks for numeric input
    if type(first_diagonal) not in [int, float] and type(second_diagonal) not in [int, float]:
        raise TypeError("The first and second diagonal must be int or float")
    if type (first_diagonal) not in [int, float]:
        raise TypeError("The first diagonal must be int or float")
    if second_diagonal not in [int, float]:
        raise TypeError("The second diagonal must be int or float")

    # checks if numeric input is whether int or float
    if first_diagonal <= 0 or second_diagonal <= 0:
        raise ValueError ("Both diagonals must be positive")

    return (first_diagonal*second_diagonal)/2

#endregion FUNCTIONS