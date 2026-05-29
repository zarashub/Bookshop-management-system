import sys

def show_menu():
    print("\n--- Bookshop Management System ---")
    print("1. Add a book")
    print("2. Show all books")
    print("3. Sell a book")
    print("4. Exit")

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    try:
        price = float(input("Enter price: $"))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid input! Price must be a number and stock must be an integer.")
        return

    books[title] = {"author": author, "price": price, "stock": stock}
    print(f"'{title}' has been added successfully!")

def show_books(books):
    if not books:
        print("No books in the system yet.")
        return

    print("\n--- Book List ---")
    for title, info in books.items():
        print(f"Title: {title}")
        print(f"Author: {info['author']}")
        print(f"Price: ${info['price']:.2f}")
        print(f"Stock: {info['stock']}")
        print("-" * 20)

def sell_book(books):
    if not books:
        print("No books available to sell.")
        return

    title = input("Enter book title to sell: ")

    if title not in books:
        print("Book not found.")
        return

    if books[title]["stock"] <= 0:
        print("Sorry, this book is out of stock.")
        return

    books[title]["stock"] -= 1
    print(f"'{title}' sold! Remaining stock: {books[title]['stock']}")

def main():
    books = {}

    print("Welcome to the Bookshop Management System!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            sell_book(books)
        elif choice == "4":
            print("Thank you for using the Bookshop Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
