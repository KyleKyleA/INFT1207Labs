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

def ellipse_area(major_axis, minor_axis):
    """Calculates area of eclipse given major and minor axes"""
    # checks for numeric inputs
    if (type(major_axis) and type(minor_axis)) not in [int, float]:
        raise TypeError("The major and minor axes must be in or float")
    if type(major_axis) not in [int, float]:
        raise TypeError("The major axis must be int or float")
    if type(minor_axis) not in [int, float]:
        raise TypeError("The minor axis must be int or float")

    # checks if numeric inputs is greater than 0
    if major_axis <0 and minor_axis<0:
        raise ValueError("Major and minor axes must be positive")
    if major_axis < 0:
        raise ValueError("Major axis must be positive")
    if minor_axis < 0:
        raise ValueError("Minor axis must be positive")

    return pi*major_axis*minor_axis
#endregion FUNCTIONS