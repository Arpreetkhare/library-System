from app.models.book_model import Book
from app.database import db

class BookCRUD:
    def __init__(self):
        pass

    def create(self, data):
        new_book = Book(
            title=data['title'],
            author=data['author'],
            published_date=data.get('published_date', None)
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book

    
    def get_by_id(self, book_id):
        return Book.query.get_or_404(book_id)

    def update(self, book_id, data):
        book = Book.query.get_or_404(book_id)
        book.title = data['title']
        book.author = data['author']
        book.published_date = data.get('published_date', None)
        db.session.commit()
        return book

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
