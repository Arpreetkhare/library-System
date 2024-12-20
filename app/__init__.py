from flask import Flask
from app.database import db, init_db
from app.routes.books import books_bp
from app.routes.members import members_bp

def create_app():
    app = Flask(__name__)

    # Update to MySQL Database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1812@localhost:3306/library_System'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)
    with app.app_context():
        init_db()

    # Register Blueprints
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(members_bp, url_prefix='/members')

    return app