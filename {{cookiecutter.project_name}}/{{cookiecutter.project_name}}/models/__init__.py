import uuid

from sqlalchemy.ext.declarative import AbstractConcreteBase


class Base(AbstractConcreteBase):
    def __init__(self, id=None, *args, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        super(Base, self).__init__(id=id, *args, **kwargs)
