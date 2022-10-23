import bcrypt

from app import db, app
from datetime import datetime
from cryptography.fernet import Fernet


def encrypt(data, postkey):
    return Fernet(postkey).encrypt(bytes(data,'utf-8'))


def decrypt(data, postkey):
    return Fernet(postkey).decrypt(data).decode('utf-8')

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    blogs = db.relationship('Post')
    postkey= db.Column(db.BLOB)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.postkey = Fernet.generate_key()

class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey(User.id), nullable=True)
    created = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(1000), nullable=False)

    def __init__(self, username, title, body, postkey):
        self.username = username
        self.title = encrypt(title, postkey)
        self.body = encrypt(body, postkey)
        self.created = datetime.now()


    def update_post(self, title, body, postkey):
        self.title = encrypt(title, postkey)
        self.body = encrypt(body, postkey)

        db.session.commit()

    def view_post(self,title, body,  postkey):
        self.title = decrypt(title, postkey)
        self.body = decrypt(body, postkey)


def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
