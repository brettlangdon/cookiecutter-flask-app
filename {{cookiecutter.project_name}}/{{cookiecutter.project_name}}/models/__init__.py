import datetime
import uuid

from sqlalchemy import event
from sqlalchemy.ext.declarative import AbstractConcreteBase

from .. import db


class Base(AbstractConcreteBase):
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False)

    def __init__(self, id=None, created_at=None, updated_at=None, *args, **kwargs):
        if id is None:
            id = str(uuid.uuid4())

        if created_at is None:
            created_at = datetime.datetime.now(tz=datetime.timezone.utc)
        if updated_at is None:
            updated_at = created_at

        super(Base, self).__init__(id=id, created_at=created_at, updated_at=updated_at, *args, **kwargs)


# Before we update our model, update its `updated_at` value
@event.listens_for(Base, 'before_update', propagate=True)
def base_update_updated_at(mapper, connection, model):
    """When we update a base model, update the `updated_at` timestamp"""
    model.updated_at = datetime.datetime.now(tz=datetime.timezone.utc)
