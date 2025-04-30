# json module is use to save & load the data.
import json
# os module is use for file handling and system operations
import os


data_file = 'library.txt'

def load_library():
    # file ko read mode mein open krega 
    if os.path.exists(data_file):
         #'r' means read mode mein open kreg..
        with open(data_file, 'r') as file:
            # json.load() function use to load the data from json file
            return json.load(file)
    return []


def save_library(library):
    # file ko write mode mein open krega
    with open(data_file, 'w') as file:
        # json format mein save krega us data ko.
        json.dump(library, file)


def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre =input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() =='yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
}    

    library.append(new_book)
    save_library(library)
    print(f"book {title} add successfully!")

def remove_book(library):
    # title of the book to remove
    title = input('Enter the title of the book to remove: ')
    initial_length = len(library)
    # sirf un book ko list mein rakhega jo user given se match nh krta.
    library = [book for book in library if book['title'].lower() != title]
    if len(library) <= initial_length:
        # library parameter remove krne ke baad update krne ke liye use kiya hai.
        save_library(library)
        # agr book remove hogai toh ye statements dega.
        print(f"book {title} removed successfully.")
    else:
        # agr book nh remove hogai toh ye statements dega.
        print(f"Book {title} not found in the library.") 

def search_library(library):
    # ye line user se confirm krti hai ke konsi (title/author) se search krna chahta hai.
    search_by =  input("Enter the by title or author:").lower()
    #user se actual search word ya phrase leti hai.
    # sirf un book ko list mein rakhega jo user given se match krta.
    search_term = input(f"Enter the {search_by}").lower()

    # library mein book ko search kregi user given input ke hisaab se.
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status ="Read" if book['read'] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}" )
    else:
        print(f"No books found in the library. {search_term} in the {search_by} field.")


def dsiplay_all_books(library):
    if library:
        for book in library:
            status ="Read" if book['read'] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}" )
    else:
        print("No more books in the library.")

def display_stats(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])  
    percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total Books: {total_books}")
    #2f means (agr %age 6.3333 hogi toh) only 6.33 Ayein ge.
    print(f"Percentage read : {percentage : 2f}")


def main():
    library = load_library()
    while True:
        print("Welcome to your Personal Library Manager!")
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display stats")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == '4':
            dsiplay_all_books(library)
        elif choice == '5':
            display_stats(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == '__main__':
    main()