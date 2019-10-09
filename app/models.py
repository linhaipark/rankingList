from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Qidian(db.Model):
    __tablename__ = 'qidian'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    author = db.Column(db.String(128), index=True)
    type = db.Column(db.String(16), index=True)
    source = db.Column(db.String(64), default="起点中文网")
    words = db.Column(db.Integer, index=True)
    click = db.Column(db.Integer, index=True)
    subscribe = db.Column(db.Integer, index=True)

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
