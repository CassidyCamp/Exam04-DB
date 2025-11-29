from library.db import Base, engine
from library.models import Author, Book, Student, Borrow
from library.services import *


# create_author('toshmat', 'It is a long established fact that a reader will be distracted by the readable content of ')

# print(get_author_by_id())

# for author in get_all_authors():
#     print(author.id, author.name)

# print(get_all_authors())
# get_all_authors()

# update_author(5, 'vali')
# update_author(6, 'sami')

# delete_author(3)

# create_book('javascript', 1, 2000, '0-4826-6793-1',)
# create_book('dart', 4, 2030)
# create_book('python', 2, 2010, '0-5350-7461-1')

# for book in get_all_books():
#     print(book.id, book.title, book.author_id)

# print(get_book_by_id(3))

# print(get_all_books())
# print(get_all_authors())

# print(search_books_by_title('ja'))

# delete_book(1)
# create_book('javascript', 1, 2000, '0-4826-6793-1',)

# create_student('ali valiyev', 'dawd')

# print(get_student_by_id(1))
# print(get_all_students())
# update_student_grade(1, 'd')















Base.metadata.create_all(engine)