from flask_security import UserMixin
from sqlalchemy.dialects.postgresql import UUID

from . import Base
from .. import db
from .user_role import user_role_map


class User(Base, db.Model, UserMixin):
    id = db.Column(UUID(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=user_role_map,
                            backref=db.backref('users', lazy='dynamic'))
