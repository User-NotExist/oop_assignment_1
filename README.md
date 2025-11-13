# Library Management System (OOP)

This document describes the classes, class attributes, and class methods used in the object-oriented implementation located at `oop_solution/library_oop.py`.

## File Structure
```│
├── README.md                          # This file
│
├── procedural_version/
│   ├── library_procedural.py         # Original procedural code
│   └── test_procedural.py            # Comprehensive test suite
│
├── oop_solution/
│   ├── library_oop.py                # Student's OOP implementation (to create)
│   └── test_oop.py                   # Tests for OOP version (to create)
```

## Classes

### `Book`
- Attributes
  - `id` — unique identifier for the book
  - `title` — book title
  - `author` — book author
  - `available_copies` — number of copies currently available for borrowing
  - `total_copies` — total number of copies owned by the library
- Methods
  - `__init__(id, title, author, available_copies)` — constructor, initializes attributes
  - `can_borrow()` -> `bool` — returns `True` if at least one copy is available
  - `available_copy()` -> `bool` — alias/duplicate check if a copy is available
  - `borrow()` -> `bool` — decrement `available_copies` if possible and return success
  - `return_()` -> `bool` — increment `available_copies` if less than `total_copies` and return success

---

### `Member`
- Attributes
  - `id` — unique identifier for the member
  - `name` — member's name
  - `email` — member's email
  - `borrowed_list` — list of borrowed book IDs
- Methods
  - `__init__(id, name, email)` — constructor, initializes attributes
  - `can_borrow()` -> `bool` — returns `True` if member has borrowed fewer than the allowed limit (3)
  - `existing_book(book_id)` -> `bool` — checks whether `book_id` is in `borrowed_list`
  - `borrow_book(book_id)` -> `bool` — add `book_id` to `borrowed_list` if allowed and return success
  - `return_book(book_id)` -> `bool` — remove `book_id` from `borrowed_list` if present and return success

---

### `Library`
- Attributes
  - `books_list` — list of `Book` instances
  - `members_list` — list of `Member` instances
  - `active_borrow_list` — list of active borrow transaction dictionaries (`member_id`, `book_id`, `member_name`, `book_title`)
- Methods
  - `__init__()` — constructor, initializes the lists
  - `add_book(id, title, author, available_copies)` — create and add a `Book` to `books_list`
  - `add_member(id, name, email)` — create and add a `Member` to `members_list`
  - `get_book(id)` -> `Book | None` — return the `Book` with matching `id` or `None`
  - `get_member(id)` -> `Member | None` — return the `Member` with matching `id` or `None`
  - `display_available_books()` — print books that have available copies
  - `display_member_books(id)` — print books borrowed by the member with `id`
  - `borrow_book(member_id, book_id)` — validate member/book, update book and member state, add transaction to `active_borrow_list`
  - `return_book(member_id, book_id)` — validate, update book and member state, remove transaction from `active_borrow_list`

---

## Referencing the Library Management System (OOP)
Put the oop_solution/library_oop.py file in your project directory. You can then import and use the classes as follows:

```python
from oop_solution.library_oop import Library, Book, Member
```

## Running Tests
Run the following command to test oop implementation:

```bash
python oop_solution/test_oop.py
```

Alternatively, to run tests in procedural implementation:

```bash
python procedural_version/test_procedural.py
```