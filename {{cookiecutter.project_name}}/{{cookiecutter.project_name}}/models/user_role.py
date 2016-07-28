from sqlalchemy.dialects.postgresql import UUID

from .. import db

user_role_map = db.Table(
    'user_role',
    db.Column('user_id', UUID(), db.ForeignKey('user.id')),
    db.Column('role_id', UUID(), db.ForeignKey('role.id')),
)
