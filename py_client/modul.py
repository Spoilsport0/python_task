from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    second_name = Column(String(45), nullable=False)
    age = Column(Integer, nullable=False)
    login = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    grade_id = Column(Integer, nullable=False)

class Research(Base):
    __tablename__ = 'research'

    id = Column(Integer, primary_key=True)
    title = Column(String(45), nullable=False)
    category = Column(String(45), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship('Person', backref='research')

class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    grade_of_research = Column(Integer, nullable=False)
    grade_of_poster = Column(Integer, nullable=False)
    grade_of_presentation = Column(Integer, nullable=False)
