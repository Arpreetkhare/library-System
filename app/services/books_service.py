from app.crud.books_crud import BookCRUD
from app.helpers.book_helpers import book_to_dict
from app.models.book_model import Book

class BookServices:
    def __init__(self):
        self.book_crud = BookCRUD()

    def create_books_service(self, data):
        """
        Creates a new book after checking if a book with the same title or ISBN already exists.

        :param data: The book data (title, author, ISBN, etc.).
        :return: The created book object.
        :raises ValueError: If a book with the same title or ISBN exists.
        :raises Exception: If there is an error during book creation.
        """
        existing_book = Book.query.filter(
            (Book.title == data.get('title')) | 
            (Book.isbn == data.get('isbn'))
        ).first()

        if existing_book:
            raise ValueError("Book with the same title or ISBN already exists.")

        try:
            book = self.book_crud.create(data)
            return book
        except Exception as e:
            raise Exception(f"Error creating book: {str(e)}")
    
    def get_books_service(self, page, per_page):
        """
        Fetches books with pagination.

        :param page: Page number.
        :param per_page: Number of books per page.
        :return: List of books for the given page.
        :raises Exception: If there is an error fetching books.
        """
        try:
            books = self.book_crud.get_all(page, per_page)
            return books
        except Exception as e:
            raise Exception(f"Error fetching books: {str(e)}")
    
    def get_book_by_id_service(self, id):
        """
        Fetches a book by its ID.

        :param id: The unique identifier of the book.
        :return: The book object.
        :raises Exception: If the book with the given ID does not exist or an error occurs.
        """
        try:
            book = self.book_crud.get_by_id(id)
            return book
        except Exception as e:
            raise Exception(f"Error fetching book with id {id}: {str(e)}")
    
    def update_book_service(self, id, data):
        """
        Updates a book with the provided data.

        :param id: The unique identifier of the book.
        :param data: The updated book data.
        :return: The updated book object.
        :raises Exception: If the book update fails.
        """
        try:
            book = self.book_crud.update(id, data)
            return book
        except Exception as e:
            raise Exception(f"Error updating book with id {id}: {str(e)}")

    def delete_book_service(self, id):
        """
        Deletes a book by its ID.

        :param id: The unique identifier of the book.
        :return: The deleted book object.
        :raises Exception: If there is an error deleting the book.
        """
        try:
            book = self.book_crud.delete(id)
            return book
        except Exception as e:
            raise Exception(f"Error deleting book with id {id}: {str(e)}")
