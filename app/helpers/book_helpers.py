
def book_to_dict(book):
    """ return the response as a dict """

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date,
        "isbn": book.isbn
    }
