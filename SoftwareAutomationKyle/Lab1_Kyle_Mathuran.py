#Lab 1 Password Generator
#Names: Kyle And Mathuran
#Date: 5/23/25
#Description: create a program which would generate a random strong
# password based on the users’ instructions. The user can decide the number of characters in
# their password along with the number of letters, digits, and special characters in their
# custom password. The program should be tested to all the extremes to ensure proper
# functioning.

#Imports
import random

# initialize CONSTANTS
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

STRING_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

STRING_SPECIAL_CHARACTERS = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+",
                             ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
                             "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

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


def generate_password(length: int, letters: int ,  digits: int, special_characters: int):
    """Generates a password based on the given parameter"""
    #This just verfies that parameters don't conflict
    if letters + digits + special_characters == length:
        raise ValueError("Sum of letters, digits, and special characters must equal total password length")


    #randomly generates a set of letters, digits, and special characters
    chosen_letters = random.choices((UPPER_CASE_LETTERS + LOWER_CASE_LETTERS), k=letters)
    chosen_digits = random.choices(STRING_DIGITS, k=digits)
    chosen_special = random.choices(STRING_SPECIAL_CHARACTERS, k=special_characters)

    #Combines the randomly generated sets and shuffles them
    password_chars = chosen_letters + chosen_digits + chosen_letters
    random.shuffle(password_chars)
    return ''.join(password_chars)
#endregion modifiers


#region wrapper
def main(password_length=None):
    # greet user and explain program
    print("Hello!")
    print("This program will generate a random password based on your specifications.\n")

    # call functions to prompt user's inputs
    password_lengths = set_length(f"Enter the length of the password (>=: {MIN_LENGTH}): ", MIN_LENGTH)
    number_of_letters = set_letters(f"Enter the number of letters in the password (b/w {MIN_LETTERS} and {MAX_LETTERS}): ",
                                    MIN_LETTERS, MAX_LETTERS)
    number_of_digits = set_digits(f"Enter the number of digits in the password (b/w {MIN_DIGITS} and {MAX_DIGITS}): ",
                                    MIN_DIGITS, MAX_DIGITS)
    number_of_special_characters = set_special_characters(f"Enter the number of special characters in the password (b/w {MIN_SPECIAL_CHARACTERS} and {MAX_SPECIAL_CHARACTERS}): ",
                                    MIN_SPECIAL_CHARACTERS, MAX_SPECIAL_CHARACTERS)


    #call function to generate and output password
    try:
        password = generate_password(password_length, number_of_letters, number_of_digits, number_of_special_characters)
        print(f"\nYour desired password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")


#region MAIN PROGRAM
if __name__ == "__main__":
    main()
    exit()
#EndRegion MAIN PROGRAM



