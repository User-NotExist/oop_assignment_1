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
