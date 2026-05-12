from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        labels = {
            'name' : 'Book Title',
            'author' : 'Author',
            'category' : 'Category',
            'publisher' : 'Publisher',
            'pub_year' : 'Publish Year',
            'av_cpy': 'Available Copy',
        }

        widgets = {
            'name' : forms.TextInput(attrs={ 'placeholder':'Enter Book Name'}),
            'author' : forms.TextInput(attrs={ 'placeholder':'Enter Author'}),
            'category' : forms.TextInput(attrs={'placeholder':'Enter Category'}),
            'publisher' : forms.TextInput(attrs={ 'placeholder':'Enter Publisher'}),
            'pub_year' : forms.DateInput(attrs={'placeholder':'Enter Publish Year' , 'type':'date'}),
            'av_cpy' : forms.NumberInput(attrs={'placeholder':'Enter Available Copy'}),
        }