from sqlalchemy import Column, Integer, String, Boolean

from db.database import Base


class User(Base):
    """ User model. """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
