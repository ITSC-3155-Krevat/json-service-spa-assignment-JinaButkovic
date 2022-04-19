from flask import Blueprint, abort, jsonify,request
from src.models import Book, db

book_router = Blueprint('book_route', __name__, url_prefix='/books')


@book_router.get('')
def get_all_books():
    all_books = Book.query.all()
    return jsonify([book.to_dict() for book in all_books])


@book_router.get('/<int:book_id>')
def get_single_book(book_id: int):
    single_book = Book.query.get(book_id)
    return jsonify(single_book.to_dict())


@book_router.post('')
def create_book():
    title = request.json.get('title', '')
    author = request.json.get('author', '')
    rating = request.json.get('rating', 0)
    
    if title == '' or author == '' or rating < 1 or rating > 5:
        abort(400)
        
    new_book = Book(title, author, rating)
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify(new_book.to_dict())


@book_router.put('/books/<int:book_id>')
def update_book(book_id: int):
    pass


@book_router.delete('/books/<int:book_id>')
def delete_book(book_id: int):
    pass
