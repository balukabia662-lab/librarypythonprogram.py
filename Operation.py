
# Operation.py
# library_system.py

GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance")
books = {}
members = []


def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        print("book with this ISBN already exists.")
        return
    if genre not in GENRES:
        print("invalid genre.")
        return
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    print(f"book '{title}' added successfully!")

def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            print("member ID already exits.")
            return
        members.append({
            "member_id": member_id,
            "name": name,
            "email": email,
            "borrowed_books": []
        })
        print(f"member '{name}' added successfully!")

def borrow_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("member not found.")
        return
    if len(member["borrowed_books"]) >=3:
        print("cannot borrowed more than 3 books.")
        return
    book = books.get(isbn)
    if not book:
        print("book not found.")
        return
    if book["available_copies"] <= 0:
        print("no copies available.")
        return
    member["borrowed_books"].append(isbn)
    book["available_copies"] -= 1
    print(f"{member['name']} borrowed '{book['title']}'")

def return_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("member not found.")
        return
    if isbn not in member["borrowed_books"]:
        print("this member did not borrowed that book.")
        return
    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    print(f"{member['name']} returned '{books[isbn]['title']}'")










