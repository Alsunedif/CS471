from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price','edition']

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise forms.ValidationError("Price must be greater than zero.")
            return price