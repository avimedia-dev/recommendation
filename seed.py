from app import create_app, db
from app.models import Product, User
from werkzeug.security import generate_password_hash

# Create the app context
app = create_app()
with app.app_context():
    # Drop all existing data and create new tables
    db.drop_all()
    db.create_all()

    # Add sample users
    user1 = User(username="john_doe", email="john@example.com", password=generate_password_hash("password123"))
    user2 = User(username="jane_doe", email="jane@example.com", password=generate_password_hash("securepass"))

    db.session.add_all([user1, user2])

    # Add sample products
    products = [
    Product(name="Laptop"),
    Product(name="Smartphone"),
    Product(name="Headphones"),
    Product(name="Smartwatch"),
    Product(name="Gaming Console")
]

    db.session.add_all(products)

    # Commit the changes to the database
    db.session.commit()

    print("Database populated successfully!")
