from django import forms
from .models import Library

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ["student", "book" , "exp_return_date" , "return_date"]


        widgets = {
            'exp_return_date' : forms.DateInput(attrs={'class':'form-control' , 'type':'date' , 'placeholder':'Expected Return Date'}),
            'return_date' : forms.DateInput(attrs={'class':'form-control' , 'type':'date' , 'placeholder':'Return Date'}  ),
        }