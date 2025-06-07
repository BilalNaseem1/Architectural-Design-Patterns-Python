Great! Here's a **beginner-friendly homework assignment** that mirrors the style of the `Batch`/`OrderLine` domain model — designed to help you **practice domain modeling** with Python and testing using `pytest`.

---

## 📝 Homework Title:

**Domain Modeling: Library Book Reservation System**

---

## 📘 Problem Statement

You’re building the backend logic for a **Library System**.

Your library has:

* **Books** with a title, author, and unique ISBN.
* **Copies** of each book (like batches), each with a unique copy ID.
* **Members** who can reserve books.

Your goal is to:

* Model the logic for **reserving a book copy**
* Keep track of which copies are **reserved or available**
* Prevent **duplicate reservations**
* Allow a reservation to be **canceled**

---

## 🎯 Requirements

### 1. `Book` class (immutable):

* `isbn: str`
* `title: str`
* `author: str`

### 2. `BookCopy` class:

* `copy_id: str`
* `isbn: str` (link to Book)
* Tracks reservation status
* Methods:

  * `reserve(member_id: str)`
  * `cancel_reservation(member_id: str)`
  * `is_reserved` property

### 3. `Library` class:

* Tracks all book copies in the system
* Can find available copies of a book by ISBN
* Can reserve a copy for a member

---

## ✅ Functional Rules to Cover in Tests

Write **pytest tests** for these rules:

1. **A book copy can be reserved if it’s not already reserved**
2. **A reserved copy cannot be reserved again**
3. **Canceling a reservation makes the copy available again**
4. **The library can find available copies for a given book**
5. **A member cannot reserve the same copy twice**

---

## 🧪 Suggested Test File: `test_library.py`

Example:

```python
def test_copy_can_be_reserved_if_not_already_reserved():
    copy = BookCopy(copy_id="copy-001", isbn="12345")
    copy.reserve("member-001")
    assert copy.is_reserved is True
```

---

## 🗂 Suggested Folder Structure

```
library_project/
├── src/
│   ├── models.py        # Domain models
├── tests/
│   └── test_library.py  # Unit tests using pytest
├── pytest.ini
```

---

## 🧠 Bonus Challenges (Optional)

* Track which member reserved the copy
* Limit number of books a member can reserve (e.g., max 3)
* Add ETA to simulate return dates like we did with `Batch.eta`

---

## 📦 Tools You’ll Practice

* Python classes and encapsulation
* `@dataclass(frozen=True)` for value objects
* Business logic in methods (`reserve`, `cancel_reservation`)
* `pytest` for writing clean, behavior-driven unit tests

---


## Hint

Absolutely! Here are hints to guide you as you build `model.py` for the **Library Book Reservation System**:

---

### ✅ Step 1: Start with the **`Book`** class

* Use a frozen `@dataclass` here.
* It’s just a **value object** — no methods needed.
* Think: What uniquely identifies a book regardless of copies?

---

### ✅ Step 2: Create the **`BookCopy`** class

* Each copy has a unique ID and belongs to a `Book` via its ISBN.
* You’ll need to **track whether it’s reserved**.
* Internally store the ID of the member who reserved it (if any).
* Add a method to **reserve a copy**, but only if it’s available.
* Add a method to **cancel** the reservation.
* Make a property for `is_reserved`.

---

### ✅ Step 3: Add the **`Library`** class

* Think of this as the "Batch Manager".
* It manages a **collection of BookCopy objects**.
* Add a method to **find available copies** by ISBN.
* Add a method to **reserve an available copy** for a member.

---

### 🔁 General Hints

* Use a `set()` or `list` to track all the `BookCopy` objects.
* Use helper methods in `Library` to encapsulate logic — e.g., searching, filtering.
* Don’t overthink the database — this is just in-memory logic.
* Follow the same separation of concerns style as you did with `Batch` and `OrderLine`.
