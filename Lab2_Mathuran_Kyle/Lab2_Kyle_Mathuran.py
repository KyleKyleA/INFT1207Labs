"""
Names: Mathuran Chandramohan, Kyle Angeles
Program: INFT 1207
Date: June 8th, 2025
Description: Program will store and retrieve information related to a user's reading list
"""
#region LIBRARIES
import csv
#endregion LIBRARIES

#region GLOBAL VARIABLES
BOOK_LIST = "books.csv"
MENU = """
------------------------------------
Main Menu
1. Add book
2. View reading list
3. Search for book
4. Quit
"""
#endregion GLOBAL VARIABLES

#region FUNCTIONS
#region mutators
def append_book(title: str, author: str, year: int):
    """Adds book to reading list provided w/ a book title, author's name, and publication year"""
    try:
        with open(BOOK_LIST, mode='a', newline='') as file:
            # appends book info to reading list
            writer = csv.writer(file)
            writer.writerow([title, author, year])
    except FileNotFoundError:
        print("No reading list is found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(e)
#endregion mutators

#region accessors
def retrieve_book():
    """Display all books in the reading list"""
    try:
        with open(BOOK_LIST, mode='r', newline='') as file:
            # initialize variables
            reader = csv.reader(file)
            found = False

            # iterates through and prints every book from reading list
            print("Your reading list: ")
            for rows in reader:
                found = True
                print_book(rows)

            # empty reading list
            if not found:
                print("Currently your reading list is empty.")
    except FileNotFoundError:
        print("Reading list is not found or listed. Try adding a book first!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(e)

def search_book(search_term: str):
    """Search for a book in the reading list by title"""
    try:
        with open(BOOK_LIST, mode='r', newline='') as file:
            # initialize variables
            reader = csv.reader(file)
            found = False

            # iterates through each line until book is found
            for rows in reader:
                if rows[0].strip().lower() == search_term.lower():
                    print("Book has been found!")
                    print_book(rows)
                    found = True
                    break

            # book not found
            if not found:
                print("Book not found!")
    except FileNotFoundError:
        print("No reading list is founded!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(e)
#endregion accessors

#region helpers
def validate_string(prompt: str, field_name: str):
    """Prompts and validate user input for a non-empty string value"""
    while True:
        # prompt user input
        string_input = input(prompt)

        # checks for empty input
        if not string_input:
            print(f"{field_name} cannot be empty!\n")
            continue

        return string_input

def validate_year(prompt: str):
    """Prompts and validates user input for a 4-digit year"""
    while True:
        # prompt user input
        year_input = input(prompt).strip()

        # checks for empty input
        if not year_input:
            print("Year cannot be empty!\n")
            continue

        # checks for non-integer input
        if not year_input.isnumeric():
            print("Year must be an integer value!\n")
            continue

        # checks for year length less than 4
        if len(year_input) != 4:
            print("Year must be a 4-digit number!\n")
            continue

        return int(year_input)

def validate_int_range(prompt: str, minimum: int, maximum: int):
    """Prompts user for integer input and checks if it's within the specified range"""
    while True:
        try:
            # prompt user for input
            int_input = int(input(prompt))

            # checks if number is within specified range
            if int_input < minimum or int_input > maximum:
                raise Exception(f"Number input must be within specified range!\n")

            return int_input
        except ValueError as v:
            print(f"{v}. Only integer values are accepted!\n")
            continue
        except Exception as e:
            print(e)
            continue

def print_book(book_info: list[str]):
    """Formats elements from the .csv line and prints them out"""
    print(f"TITLE: {book_info[0].strip(",")}, AUTHOR: {book_info[1].strip(",")}, YEAR: {book_info[2]}")
#endregion helpers

#region wrappers
def menu():
    """Runs reading list menu for main program"""
    while True:
        # greet user and prompt action
        print(MENU)
        menu_input = validate_int_range("Pick option (1-4): ", 1, 4)

        print("")

        # executes user's request
        if menu_input == 1:
            title_input = validate_string("Enter book title: ", "Title")
            print("")
            author_input = validate_string("Enter book's author: ", "Author")
            print("")
            year_input = validate_year("Enter publication year: ")
            append_book(title_input, author_input, year_input)
        elif menu_input == 2:
            retrieve_book()
        elif menu_input == 3:
            book_input = validate_string("Enter book title: ", "Title")
            print("")
            search_book(book_input)
        elif menu_input == 4:
            break
#endregion wrappers
#endregion FUNCTIONS

#region MAIN PROGRAM
if __name__ == "__main__":
    # greet user and explain program
    print('-'*40)
    print("This program can store and retrieve books to your reading list!")
    print('-' * 40)

    menu()

    #bade user farewell
    print("Thank you for using program!")
    exit()
#endregion MAIN PROGRAM
