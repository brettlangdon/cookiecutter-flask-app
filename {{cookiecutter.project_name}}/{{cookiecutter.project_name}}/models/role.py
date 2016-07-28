from flask_security import RoleMixin
from sqlalchemy.dialects.postgresql import UUID

from . import Base
from .. import db


class Role(Base, db.Model, RoleMixin):
    id = db.Column(UUID(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
