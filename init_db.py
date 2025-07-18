from app import create_app, db
from app.models import Employee

def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
    print("Database initialized.")

if __name__ == '__main__':
    init_db()