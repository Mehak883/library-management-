from django import forms
from django.contrib.auth.models import User
from . import models
from register.models import profile

class ReturnBookForm(forms.Form):
     # it will make a direct drop down list fetch all books in a drop down menu
    id2 = forms.ModelChoiceField(queryset=models.IssueBook.objects.all(), empty_label="Student Name and Book Name ", to_field_name="bookid", label="Book ( StudentName and bookid)")
     # it will make a direct drop down list fetch all subscribers in a drop down menu
    # name2 = forms.ModelChoiceField(queryset=models.IssueBook.objects.all(), empty_label="Name ", to_field_name="email", label="Students Details( Name and Email )")

    id2.widget.attrs.update({'class': 'form-control'})
    # name2.widget.attrs.update({'class':'form-control'})
