from django import forms
from apps.bookmodule import models
from .models import *
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book  # tell form that model to map
        fields = ['title', 'price', 'edition', 'author']  # tell form what to map from model


class DeleteBookForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Deletion")


# lab10
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


# task2
class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['address']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['description', 'image']



