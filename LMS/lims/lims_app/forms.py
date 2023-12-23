from django import forms
from .models import *

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}) ,
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =[
            'title',
            'author',
            'photo_author',
            'photo_book',
            'pages',
            'price',
            'retal_price_day',
            'status',
            'category',
        ]
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'photo_author':forms.FileInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day':forms.NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }