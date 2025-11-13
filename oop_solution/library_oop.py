# Library Management System

class Book:
    def __init__(self, id, title, author, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = available_copies

    def can_borrow(self):
        if self.available_copies > 0:
            return True
        return False

    def available_copy(self):
        if self.available_copies > 0:
            return True
        return False

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True

        return False

    def return_(self):
        if self.total_copies > self.available_copies:
            self.available_copies += 1
            return True

        return False


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_list = []

    def can_borrow(self):
        if len(self.borrowed_list) >= 3:
            return False
        return True

    def existing_book(self, book_id):
        if book_id in self.borrowed_list:
            return True
        return False

    def borrow_book(self, book_id):
        if not self.existing_book(book_id) and self.can_borrow():
            self.borrowed_list.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        if self.existing_book(book_id):
            self.borrowed_list.remove(book_id)
            return True
        return False


class Library:
    def __init__(self):
        self.books_list = []
        self.members_list = []
        self.active_borrow_list = []

    def add_book(self, id, title, author, available_copies):
        book = Book(id, title, author, available_copies)
        self.books_list.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, id, name, email):
        member = Member(id, name, email)
        self.members_list.append(member)
        print(f"Member '{name}' registered successfully!")

    def get_book(self, id):
        for book in self.books_list:
            if book.id == id:
                return book
        return None

    def get_member(self, id):
        for member in self.members_list:
            if member.id == id:
                return member
        return None

    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books_list:
            if book.available_copy():
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self, id):
        member = self.get_member(id)

        if member is None:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if member.borrowed_list is None:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_list:
                book = self.get_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")

    def borrow_book(self, member_id, book_id):
        member = self.get_member(member_id)

        if member is None:
            print("Error: Member not found!")
            return

        book = self.get_book(book_id)

        if book is None:
            print("Error: Book not found!")
            return

        if not book.available_copy():
            print("Error: No copies available!")
            return

        if not member.can_borrow():
            print("Error: Member has reached borrowing limit!")
            return

        book.borrow()
        member.borrow_book(book_id)

        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member.name,
            'book_title': book.title
        }
        self.active_borrow_list.append(transaction)

        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id, book_id):
        member = self.get_member(member_id)
        book = self.get_book(book_id)

        if member is None or book is None:
            print("Error: Member or book not found!")
            return

        if member.existing_book(book_id):
            print("Error: This member hasn't borrowed this book!")
            return

        book.return_()
        member.return_book(book_id)

        for i, transaction in enumerate(self.active_borrow_list):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.active_borrow_list.pop(i)
                break

        print(f"{member.name} returned '{book.title}'")
