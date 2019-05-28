#!venv/bin/python
from xd import db
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
