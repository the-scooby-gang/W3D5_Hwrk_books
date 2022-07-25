from flask import render_template
from app import app
from models.list import books
from models.book import Book

@app.route('/books')
def index():
    return render_template('tasks/index.html', title = 'Todays Homework', books = books)
