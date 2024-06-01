from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguracja bazy danych
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import modeli
from models import ShoppingItem


@app.route('/')
def index():
    shopping_list = ShoppingItem.query.all()
    return render_template('index.html', shopping_list=shopping_list)


@app.route('/add', methods=['POST'])
def add():
    item_name = request.form.get('item')
    if item_name:
        new_item = ShoppingItem(name=item_name)
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
