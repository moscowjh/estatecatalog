import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String
from sqlalchemy.dialects.postgresql import INTEGER, TEXT
"""    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    picture = Column(TEXT, nullable=False)


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))


class Items(Base):
    __tablename__ = 'items'

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=True)
    value = Column(INTEGER, nullable=True)
    quantity = Column(INTEGER, nullable=True)
    disposition = Column(TEXT, nullable=True)
    image = Column(TEXT, nullable=True)
    category_id = Column(INTEGER, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    """Return object data in easily serializeable format"""
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'value': self.value,
            'quantity': self.quantity,
            'disposition': self.disposition,
            }


engine = create_engine('postgresql:///estatecatalog')

Base.metadata.create_all(engine)
