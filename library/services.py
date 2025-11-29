from .models import Author, Student, Borrow, Book
from sqlalchemy.orm import sessionmaker
from .db import get_db


def save_db(parm):
    with get_db() as session:
        session.add(parm)
        session.commit()

def create_author(name: str, bio: str = None) -> Author:
    """Yangi muallif yaratish"""
    author = Author(name=name, bio=bio)
    save_db(author)

def get_author_by_id(author_id: int) -> Author | None:
    """ID bo'yicha muallifni olish"""
    with get_db() as session:
        return session.query(Author).filter(Author.id==author_id).first()
    
def get_all_authors() -> list[Author]:
    """Barcha mualliflar ro'yxatini olish"""
    with get_db() as session:
        return session.query(Author).all()

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    with get_db() as session:
        author = session.query(Author).filter(Author.id==author_id).first()
        
        if author:
            author.name = name if name else author.name
            author.bio = bio if bio else author.bio
            
            session.add(author)
            session.commit()

def delete_author(author_id: int) -> bool:
    """Muallifni o'chirish (faqat kitoblari bo'lmagan holda)"""
    with get_db() as session:
        author = session.query(Author).filter(Author.id==author_id).first()
        if author:
            session.delete(author)
            session.commit()


# Book 
def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    """Yangi kitob yaratish"""
    b = Book(
        title=title,
        author_id=author_id,
        published_year=published_year,
        isbn=isbn
    )
    save_db(b)

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    with get_db() as session:
        return session.query(Book).filter(Book.id==book_id).first()

def get_all_books() -> list[Book]:
    """Barcha kitoblar ro'yxatini olish"""
    with get_db() as session:
        return session.query(Book).all()

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni sarlavha bo'yicha qidirish (partial match)"""
    with get_db() as session:
        return session.query(Book).filter(Book.title.like(f'%{title}%')).all()

def delete_book(book_id: int) -> bool:
    """Kitobni o'chirish"""
    with get_db() as session:
        book = session.query(Author).filter(Book.id==book_id).first()
        if book:
            session.delete(book)
            session.commit()

# Student
def create_student(full_name: str, email: str, grade: str = None) -> Student:
    """Yangi talaba ro'yxatdan o'tkazish"""
    stu = Student(full_name=full_name, email=email, grade=grade)
    save_db(stu)

def get_student_by_id(student_id: int) -> Student | None:
    """ID bo'yicha talabani olish"""
    with get_db() as session:
        return session.query(Student).filter(Student.id==student_id).first()

def get_all_students() -> list[Student]:
    """Barcha talabalar ro'yxatini olish"""
    with get_db() as session:
        return session.query(Student).all()

def update_student_grade(student_id: int, grade: str) -> Student | None:
    """Talaba sinfini yangilash"""
    with get_db() as session:
        stu = session.query(Student).filter(Student.id==student_id).first()
        
        if stu:
            stu.grade = grade if grade else stu.grade
        
        session.add(stu)
        session.commit()
    

def borrow_book(student_id: int, book_id: int) -> Borrow | None:
    """
    Talabaga kitob berish
    
    Quyidagilarni tekshirish kerak:
    1. Student va Book mavjudligini
    2. Kitobning is_available=True ekanligini
    3. Talabada 3 tadan ortiq qaytarilmagan kitob yo'qligini yani 3 tagacha kitob borrow qila oladi
    
    Transaction ichida:
    - Borrow yozuvi yaratish
    - Book.is_available = False qilish
    - due_date ni hisoblash (14 kun)
    
    Returns:
        Borrow object yoki None (xatolik bo'lsa)
    """
    with get_db() as session:
        if (
            session.query(Student).filter(Student.id==student_id) != None and
            session.query(Book).filter(Book.id==book_id) != None
        ):
            brow = Borrow(student_id, book_id)