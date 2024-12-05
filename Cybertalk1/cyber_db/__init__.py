from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """Initialize the database with the given Flask app."""
    db.init_app(app)
    with app.app_context():
        # Import models at runtime to avoid circular imports
        from Cybertalk1.cyber_db.models import User
        db.create_all()
        print("Database initialized!")

