import db


def get_all_books():
    pass


def add_new_book(name, author, year):
    print(f'name: {name}, author: {author}, year: {year}')
    # TODO:  write params to database


class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    author = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Book %r>' % self.name