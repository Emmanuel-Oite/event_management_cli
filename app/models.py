# models.py

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    location = Column(String)  
    attendees = relationship('Attendee', back_populates='event')

class Attendee(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship('Event', back_populates='attendees')

# Initialize the database
engine = create_engine('sqlite:///event_management.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
