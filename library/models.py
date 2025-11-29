from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship 
from .db import Base




class Author(Base):
    __tablename__='Author'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(length=100), nullable=False)
    bio = Column('bio', Text)
    created_at = Column('created_at', DateTime, default=datetime.now)
    
    book = relationship('Book', back_populates="author")
    
    def __repr__(self):
        return f"Author(id={self.id}, name={self.name}, bio={self.bio})"

    def __str__(self):
        return f"Author(id={self.id}, name={self.name}, bio={self.bio})"
    



class Book(Base):
    __tablename__='Book'
    
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(length=200), nullable=False)
    author_id = Column('author_id', Integer, ForeignKey('Author.id'))
    published_year = Column('published_year', Integer, nullable=False)
    isbn = Column('isbn', String(length=13), unique=True)
    is_available = Column('is_available', Boolean, default=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

    author = relationship('Author', back_populates="book")
    borrow = relationship('Borrow', back_populates="book")
    
    def __str__(self):
        return 'Book (id: {}, title: {}, author_id: {})'.format(self.id, self.title, self.author_id)
    
    def __repr__(self):
        return 'Book (id: {}, title: {}, author_id: {})'.format(self.id, self.title, self.author_id)



class Student(Base):
    __tablename__='Student'
    
    id = Column('id', Integer, primary_key=True)
    full_name = Column('full_name', String(length=150), nullable=False)
    email = Column('email', String(length=100), unique=True, nullable=False) 
    grade = Column('grade', String(length=20))
    registered_at = Column('registered_at', DateTime, default=datetime.now)
    
    borrow = relationship('Borrow', back_populates="student")
    
    def __str__(self):
        return f"Student(id={self.id}, full_name='{self.full_name}', email='{self.email}', grade='{self.grade}')"
    
    def __repr__(self):
        return f"Student(id={self.id}, full_name='{self.full_name}', email='{self.email}', grade='{self.grade}')"




class Borrow(Base):
    __tablename__='Borrow'
    
    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('Student.id'))
    book_id = Column('book_id', ForeignKey('Book.id'))
    borrowed_at = Column('borrowed_at', DateTime, default=datetime.now)
    due_date = Column('due_date', DateTime, )
    returned_at = Column('returned_at', DateTime)
    
    student = relationship('Student', back_populates="borrow")
    book = relationship('Book', back_populates="borrow")

