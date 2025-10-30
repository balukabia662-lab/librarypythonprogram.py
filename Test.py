# test.py
from Operation import add_book, add_member, borrow_book, return_book, books, members

def test_library_system():
    # Reset library data
    books.clear()
    members.clear()

    # Test adding a book
    add_book("001", "Atomic Habits", "James Clear", "Non-Fiction", 5)
    assert "001" in books
    assert books["001"]["available_copies"] == 5

    # Test adding a member
    add_member(1, "Mbalu Kabia", "mbalu@example.com")
    assert any(m["member_id"] == 1 for m in members)

    # Test borrowing a book
    borrow_book(1, "001")
    assert books["001"]["available_copies"] == 4
    assert "001" in members[0]["borrowed_books"]

    # Test returning a book
    return_book(1, "001")
    assert books["001"]["available_copies"] == 5
    assert "001" not in members[0]["borrowed_books"]

    # Test borrowing more than 3 books
    add_book("002", "Book 2", "Author 2", "Fiction", 2)
    add_book("003", "Book 3", "Author 3", "Mystery", 2)
    add_book("004", "Book 4", "Author 4", "Romance", 2)
    borrow_book(1, "001")
    borrow_book(1, "002")
    borrow_book(1, "003")
    borrow_book(1, "004")  # Should fail
    assert len(members[0]["borrowed_books"]) == 3

    print("All tests passed!")

if __name__ == "_main_":
    test_library_system()