from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# db = sqlite3.connect('day63/sqlite3-project/books-collection.db')

# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
db.create_all()


# Create record
new_book = Book(id=1, title="Scarecrow", author="Matthew Reilly", rating=9.2)
db.session.add(new_book)
db.session.commit()