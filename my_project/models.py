from my_project import db
from wtforms.validators import Regexp
from flask_login import UserMixin

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer,autoincrement= True, nullable=False)
    title = db.Column(db.String(30), nullable=False, unique=True,info={"validators": Regexp("^[A-Za-z0-9_-]*$")})
    imgfile = db.Column(db.String(30),nullable=False)
    website = db.Column(db.String(30),nullable=True)
    github_url = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    long_desc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Project.title : {self.title}>"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(30),nullable=False,unique=True)
    password_hash=db.Column(db.String(100),nullable=False)
    def __repr__(self):
        return f"<User username: {self.username}>"

