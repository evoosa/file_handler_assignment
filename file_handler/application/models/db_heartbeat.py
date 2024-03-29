import datetime

from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBHeartbeat(Base):
    """Data model for files. each file has a unique ID, and a filename"""

    __tablename__ = 'heartbeats_table'
    id = Column(
        Integer,
        primary_key=True
    )
    timestamp = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        unique=True,
        nullable=False
    )
