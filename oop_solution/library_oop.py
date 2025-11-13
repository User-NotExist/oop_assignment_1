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
