from flask import Blueprint, request, jsonify
from app.services.books_service import BookServices
from app.helpers.book_helpers import book_to_dict


books_bp = Blueprint('books', __name__)

@books_bp.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    book_service = BookServices()
    book = book_service.create_books_service(data)
    return jsonify({"message": "Book created successfully!", "book": book_to_dict(book)}), 201
    



@books_bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    book_service = BookServices()
    book = book_service.get_book_by_id_service(id)
    return jsonify(book_to_dict(book))


@books_bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
  
    data = request.get_json()
    book_service = BookServices()
    book = book_service.update_book_service(id, data)
    return jsonify({"message": "Book updated successfully!", "book": book_to_dict(book)})

@books_bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    
    book_service = BookServices()
    book_service.delete_book_service(id)
    return jsonify({"message": "Book deleted successfully!"})