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
    path('lab9_part2/deleteBook/<int:bookId>/', views.delete_book, name='books.delete_book'),

    ##lab 10
    path('students/', views.student_list, name='books.students.list'),
    path('students/add/', views.student_add, name='books.students.add'),
    path('students/edit/<int:id>/', views.student_edit, name='books.students.edit'),
    path('students/delete/<int:id>/', views.student_delete, name='books.students.delete'),

    path('students2/', views.student2_list, name='books.students2.list'),
    path('students2/add/', views.student2_add, name='books.students2.add'),
    path('students2/edit/<int:id>/', views.student2_edit, name='books.students2.edit'),
    path('students2/delete/<int:id>/', views.student2_delete, name='books.students2.delete'),

    path('images/', views.images, name='books.images'),
    path('images/add/', views.images_add, name='books.images.add'),

    #lab 12

    path('lab12/task1', views.lab_task1, name="books.task1"),
    path('lab12/task2', views.lab_task2, name="books.task2"),
    path('lab12/task3', views.lab_task3, name="books.task3"),
    path('lab12/task4', views.lab_task4, name="books.task4")


]

