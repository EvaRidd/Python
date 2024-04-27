from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///towns.db'
db = SQLAlchemy(app)

class Town(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(200), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)


def __repr__(self):
    return '<Town %r>' % self.id


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'post':
        city = request.form['city']
        visit_date = request.form['visit_date']

        new_town = Town(city=city, visit_date=visit_date)
        db.session.add(new_town)
        db.session.commit()

    towns = Town.query.all()
    return render_template('index.html', towns=towns)


if __name__ == '__main__':
    app.run(debug=True)

