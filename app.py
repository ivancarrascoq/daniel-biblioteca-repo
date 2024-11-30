from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from model.book import db, Book, add_dummy_data

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple login logic for demonstration purposes
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/all', methods=['GET'])
def all():
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page=page, per_page=10, error_out=False)
    total = Book.query.count()
    next_url = url_for('all', page=books.next_num) if books.has_next else None
    prev_url = url_for('all', page=books.prev_num) if books.has_prev else None
    return render_template('all.html', books=books.items, total=total, next_url=next_url, prev_url=prev_url, page=page)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        # books = Book.query.filter(Book.title.contains(query) | Book.author.contains(query)).all()
        books = Book.query.filter(Book.title.contains(query) | Book.author.contains(query))[:10]
    else:
        # books = Book.query.all()
        books = Book.query[:10]
    total = Book.query.count()
    return render_template('search.html', books=books, total=total)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']
        db.session.commit()
        return redirect(url_for('search'))
    return render_template('update.html', book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('search'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # add_dummy_data()
    app.run(debug=True)
