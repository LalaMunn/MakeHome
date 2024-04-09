from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key= 'abcdefghijklmnopnguyentuyetnhi00#@!$%asbnq'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nt20042008@localhost/mkhome?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

db = SQLAlchemy(app=app)

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()