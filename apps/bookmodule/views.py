from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django import forms
from .forms import *
from django.db.models import Count, Sum, Avg, Max, Min, Q
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index2(request, val1 = 0):
    return render(request, "bookmodule/index2.html", {"value":val1})

def index(request):
    return render(request, "bookmodule/index.html")



def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html', {"bookId":bookId})

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained: newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    else:
        return render(request, 'bookmodule/search.html')

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='al')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def task1(request):
    books = Book.objects.filter(price__lte=50    )  # Books with price ≤ 50
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains="qu") | Q(author__icontains="qu"))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=2) & ~(Q(title__icontains="qu") | Q(author__icontains="qu"))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')  # Order books by title
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})


def listBooks(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/listBooks.html',{'books': mybooks})
def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price', 0.0))
        edition = int(request.POST.get('edition', 1))

        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('books.listBooks')

    return render(request, 'bookmodule/addBook.html')
def editBook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price', 0.0))
        book.edition = int(request.POST.get('edition', 1))
        book.save()
        return redirect('books.listBooks')
    return render(request, 'bookmodule/editBook.html', {'book': book})

def deleteBook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books.istBooks')





def list_books(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/list_book.html', {'books': mybooks})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.list_books')
    else:
        form = BookForm()
    return render(request, 'bookmodule/book_form.html', {'form': form, 'action': 'Add'})



def edit_book(request, bookId):
    book = get_object_or_404(Book, id=bookId)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/book_form.html', {'form': form, 'action': 'Edit'})

def delete_book(request, bookId):
    book = get_object_or_404(Book, id=bookId)
    if request.method == 'POST':
        book.delete()
        return redirect('books.list_books')
    return render(request, 'bookmodule/book_confirm_delete.html', {'book': book})




def student_list(request):
    students = Student.objects.select_related('address').all()
    return render(request, 'bookmodule/students/student_list.html', {'students': students})


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.students.list')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/students/student_form.html', {'form': form})

@login_required
def student_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('books.students.list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/students/student_form.html', {'form': form})


def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('books.students.list')



def student2_list(request):
    students = Student2.objects.prefetch_related('addresses').all()
    return render(request, 'bookmodule/students/student2_list.html', {'students': students})


def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.students2.list')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/students/student2_form.html', {'form': form})

@login_required
def student2_edit(request, id):
    student = get_object_or_404(Student2, pk=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('books.students2.list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/students/student2_form.html', {'form': form})


def student2_delete(request, id):
    student = get_object_or_404(Student2, pk=id)
    student.delete()
    return redirect('books.students2.list')


def images(request):
    images = Images.objects.all()
    return render(request, 'bookmodule/students/images.html', {'images': images})


def images_add(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books.images')
    else:
        form = ImagesForm()
    return render(request, 'bookmodule/students/add.html', {'form': form})

def lab_task1(request):
    return render(request,'bookmodule/lab12/task1.html')
def lab_task2(request):
    return render(request,'bookmodule/lab12/task2.html')
def lab_task3(request):
    return render(request,'bookmodule/lab12/task3.html')
def lab_task4(request):
    return render(request,'bookmodule/lab12/task4.html')

