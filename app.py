from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import ShoppingItem

app = Flask(__name__)

# Konfiguracja bazy danych
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    shopping_list = ShoppingItem.query.all()
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add', methods=['POST'])
def add():
    item_name = request.form.get('item')
    is_monika = 'is_monika' in request.form
    is_jacek = 'is_jacek' in request.form
    if item_name:
        new_item = ShoppingItem(name=item_name, is_monika=is_monika, is_jacek=is_jacek)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    item = ShoppingItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)