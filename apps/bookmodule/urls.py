from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('html5/links/',views.links, name="books.html5.links"),
 path('html5/text/formatting', views.formatting, name="books.html5.Text_Formatting"),
 path('html5/listing', views.listing, name="books.html5.links"),
 path('html5/tables', views.table, name="books.html5.tables"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
]

