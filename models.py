from sqlalchemy import Column, Boolean, Integer, Text, DateTime, ForeignKey
from database import Base
from flask_login import UserMixin
from hash_passwords import check_hash, make_hash


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    def __init__(self, username=None, password=None, active=False):
        self.username = username
        self.password = password
        self.active = active

    def is_active(self):
        return self.active

    def get(id):
        if self.id == id:
            return self
        else:
            return None

    def valid_password(self, password):
        """Check if provided password is valid."""
        return check_hash(password, self.password)

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id, self.username)

