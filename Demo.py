
#
# demo.py
from Operation import add_book, add_member, borrow_book, return_book, books, members
#---- Demo actions ---

# Add sample book and member
add_book("001", "Atomic Habits", "James Clear", "Non-Fiction", 5)
add_member(1, "Mbalu Kabia", "mbalu@example.com")

# Borrow and return book
borrow_book(1, "001")
return_book(1, "001")

# show current library state
print("\nCurrent books:", books)
print("Current members:", members)

input("\nPress Enter to exit...")