from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.listBooks, name="books.list_books"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('search/', views.search, name="books.search"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/links/', views.links, name="books.links"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),

    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),

    ##lab 8
    path('lab8/task1', views.task1, name='books.task1'),
    path('lab8/task2', views.task2, name='books.task2'),
    path('lab8/task3', views.task3, name='books.task3'),
    path('lab8/task4', views.task4, name='books.task4'),
    path('lab8/task5', views.task5, name='books.task5'),

    ##lab 9

    path('lab9_part1/addBook', views.addBook, name="books.addBook"),
    path('lab9_part1/listBooks', views.listBooks, name='books.listBooks'),
    path('lab9_part1/editBook/<int:id>', views.editBook, name='books.editBook'),
    path('lab9_part1/deleteBook/<int:id>', views.deleteBook, name='books.deleteBook'),

    path('lab9_part2/listBooks', views.list_books, name='books.list_books'),
    path('lab9_part2/addBook/', views.add_book, name='books.add_book'),
    path('lab9_part2/editBook/<int:bookId>/', views.edit_book, name='books.edit_book'),
    path('lab9_part2/deleteBook/<int:bookId>/', views.delete_book, name='books.delete_book')

]

