from db import db


class ShoppingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_monika = db.Column(db.Boolean, default=False)
    is_jacek = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<ShoppingItem {self.name}>'
