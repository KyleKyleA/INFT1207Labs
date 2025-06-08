# global variables
import csv

BOOK_LIST = "books.csv"


# appending a book (Mathuran)
# retrieve book (kyle)
def retrieve_book():
    try:
        with open(BOOK_LIST, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            print("\nYour reading list: ")
            found = False
        for rows in reader:
            found = True
            print(f"Title:  {rows[0]}, Author: {rows[1]}, Year{rows[2]}")
        if not found:
            print("Currently your reading list is empty.")
    except ValueError:
        print("\nReading list is not found or listed. try adding a book first.")


# search book (Kyle)
def search_book(search_term):
    try:
        with open(BOOK_LIST, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for rows in reader:
                if rows[0].strip().lower() == search_term.lower():
                    print(f"Book has been found! Title:  {rows[0]}, Author: {rows[1]}, Year{rows[2]} ")
                    found = True
                    break
            if not found:
                print("Book not found.")
    except ValueError:
        print("No reading list is founded. ")

# menu (Mathuran)
# main function
