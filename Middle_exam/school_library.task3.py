books = input().split("&")

while True:
    command = input()
    if command == "Done":
        break
    split_command = command.split(" | ")
    action = split_command[0]

    if action == "Add Book":
        book = split_command[1]
        if book not in books:
            books.insert(0, book)

    elif action == "Take Book":
        book = split_command[1]
        if book in books:
            books.remove(book)

    elif action == "Swap Books":
        book1 = split_command[1]
        book2 = split_command[2]
        if book1 in books and book2 in books:
            index_book1 = books.index(book1)
            index_book2 = books.index(book2)
            books[index_book1], books[index_book2] = books[index_book2], books[index_book1]

    elif action == "Insert Book":
        book_name = split_command[1]
        if book_name not in books:
            books.append(book_name)

    elif action == "Check Book":
        index = int(split_command[1])
        if index in range(len(books)):
            print(books[index])

print(", ".join(books))
