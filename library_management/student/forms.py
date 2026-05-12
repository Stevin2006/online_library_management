from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'gender':'Gender',
            'email':'Email Address',
            'reg_no':'Registration Number',
            'ph_no':'Phone Number',
            'address':'Address',

        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Last Name'}),
             'gender': forms.Select(attrs={'class':'form-control' , 'placeholder':'Gender'}),
            'email': forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Email Address'}),
            'reg_no': forms.NumberInput(attrs={'class':'form-control' , 'placeholder':'Registration Number'}),
            'ph_no': forms.NumberInput(attrs={'class':'form-control' , 'placeholder':'Phone Number'}),
            'address': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Address'}),
        }
