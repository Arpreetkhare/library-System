from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    from app.models.book_model import Book
    from app.models.member_model import Member
    db.create_all()
