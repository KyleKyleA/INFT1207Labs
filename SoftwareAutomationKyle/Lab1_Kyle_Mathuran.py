#Lab 1 Password Generator
#Names: Kyle And Mathuran
#Date: 5/23/25
#Description: create a program which would generate a random strong
# password based on the users’ instructions. The user can decide the number of characters in
# their password along with the number of letters, digits, and special characters in their
# custom password. The program should be tested to all the extremes to ensure proper
# functioning.

#region IMPORTS
import random
import string
#endregion IMPORTS

#region GLOBAL VARIABLES
MIN_LENGTH = 8

MIN_LETTERS = 0
MAX_LETTERS = 9

MIN_DIGITS = 0
MAX_DIGITS = 6

MIN_SPECIAL_CHARACTERS = 0
MAX_SPECIAL_CHARACTERS = 2

UPPER_CASE_LETTERS = ("A", "B", "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",
           "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "S",  "T", "U",
           "V", "W", "X", "Y", "Z")

LOWER_CASE_LETTERS = ("a",  "b",  "c",  "d",  "e",  "f",  "g",  "h", "i", "j",
                      "k", "l","m", "n", "o",  "p",   "q",   "s",   "t",   "u",
                      "v",   "w",   "x",   "y",   "z")
#endregion

#region FUNCTIONS
# modifiers
def set_length (prompt: str, minimum: int):
    """Gets, verifies, and returns user's valid length input"""
    while True:
        # checks if int value is entered
        try:
            # prompt user for input
            length_output = int(input(prompt))

            # checks if value is at least or greater than min. requirement
            if length_output >= minimum:
                return length_output
            else:
                raise Exception("Number is not large enough!")
        except ValueError as v:
            print(f"{v}. Enter an integer value!")
        except Exception as e:
            print(e)

def set_letters (prompt: str, minimum: int, maximum: int):
    """Gets, verifies, and returns user's input for number of letters"""
    while True:
        # checks if int value is entered
        try:
            # prompt user for input
            letters_output = int(input(prompt))

            # checks if value is within range
            if minimum <= letters_output <= maximum:
                return letters_output
            else:
                raise Exception("Number is not within range!")
        except ValueError as v:
            print(f"{v}. Enter an integer value!")
        except Exception as e:
            print(e)

def set_digits (prompt: str, minimum:int, maximum:int):
    """Gets, verifies, and returns user's input for number of digits"""
    while True:
        # checks if int value is entered
        try:
            # prompt user for input
            digits_output = int(input(prompt))

            # checks if value is within range
            if minimum <= digits_output <= maximum:
                return digits_output
            else:
                raise Exception("Number is not within range!")
        except ValueError as v:
            print(f"{v}. Enter an integer value!")
        except Exception as e:
            print(e)

def set_special_characters (prompt: str, minimum: int, maximum: int):
    """Gets, verifies, and returns user's input for number of special characters"""
    while True:
        # checks if int value is entered
        try:
            # prompt user for input
            special_characters_output = int(input(prompt))

            # checks if value is within range
            if minimum <= special_characters_output <= maximum:
                return special_characters_output
            else:
                raise Exception("Number is not within range!")
        except ValueError as v:
            print(f"{v}. Enter an integer value!")
        except Exception as e:
            print(e)

# def generate_password(int length, int letters, int digits, int special_characters)

# wrapper
def main():
    # greet user and explain program
    print("Hello!")
    print("This program will generate a random password based on your specifications.\n")

    # call functions to prompt user's inputs
    password_length = set_length(f"Enter the length of the password (>=: {MIN_LENGTH}): ", MIN_LENGTH)
    number_of_letters = set_letters(f"Enter the number of letters in the password (b/w {MIN_LETTERS} and {MAX_LETTERS}): ",
                                    MIN_LETTERS, MAX_LETTERS)
    number_of_digits = set_digits(f"Enter the number of digits in the password (b/w {MIN_DIGITS} and {MAX_DIGITS}): ",
                                    MIN_DIGITS, MAX_DIGITS)
    number_of_special_characters = set_special_characters(f"Enter the number of special characters in the password (b/w {MIN_SPECIAL_CHARACTERS} and {MAX_SPECIAL_CHARACTERS}): ",
                                    MIN_SPECIAL_CHARACTERS, MAX_SPECIAL_CHARACTERS)

    # call function to generate and output password

#endregion FUNCTIONS

#region MAIN PROGRAM
main()
exit()
#endregion MAIN PROGRAM