from dataclasses import dataclass

# DOMAIN
@dataclass(frozen=True)
class Books:
    isbn: str  # unique identifier of book
    title: str
    author: str


# ENTITY
class BookCopy:
    def __init__(self, copy_id, isbn):
        self.copy_id = copy_id
        self.isbn = isbn

    def reserve_book(self)
        

# AGGREGATE
class Library