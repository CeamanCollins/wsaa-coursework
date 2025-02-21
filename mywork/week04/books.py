import apimodule

books = apimodule.get_books()
total = sum(book['price'] for book in books)
count = len(books)

avg = total/count

print(f"{avg:.2f}")

print(apimodule.get_books())

# print(apimodule.delete_book(602))
# print(apimodule.delete_book(603))
