from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Book, Student, BookIssued


class IssueBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label="Book Name [ISBN]", to_field_name="isbn", label="Book (Name and ISBN)")
    name2 = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Name [Branch] [Class] [Roll No]", to_field_name="user", label="Student Details")
    
    isbn2.widget.attrs.update({'class': 'form-control'})
    name2.widget.attrs.update({'class':'form-control'})

class CreateBookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        
        
class Edit_Profile(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', 'image',)
        




class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password',   'first_name', 'last_name')

class Student_Reg_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class IssuedBooksForm(forms.ModelForm):
    
    class Meta:
        model = BookIssued
        fields = ("student", "book")