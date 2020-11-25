from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from django.contrib.admin.widgets import AdminTimeWidget
from tempus_dominus.widgets import TimePicker
from .models import SaleSize, Ingredient, Category, Menu, User, Store, Ingredient_Category


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'size': 15}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'size': 15}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 20}))

    class Meta:
        model = User
        fields = ('email','first_name','last_name')

    def clean_user(self):
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'category', 'ingredient', 'salesize', 'image')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('ingredient_name', 'Ingredient_category', 'image')

class IngredientCategoryForm(forms.ModelForm):
    class Meta:
        model = Ingredient_Category
        fields = ('name',)
        
class SalesizeForm(forms.ModelForm):
    class Meta:
        model = SaleSize
        fields = ('size','price')

class StoreForm(forms.ModelForm):
    detail = forms.CharField(widget=forms.Textarea(attrs={'rows': 1,'cols': 40,'style': 'height: 4em;'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 1,'cols': 40,'style': 'height: 6em;'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email', 'size': 15}),required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'phone', 'size': 15}),required=False)
    fbpage = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Facebook page', 'size': 15}),required=False)
    lineac = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Line account', 'size': 15}),required=False)
    igac = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'IG account', 'size': 15}),required=False)
    open_time = forms.TimeField(widget=forms.TimeInput(attrs={'id': 'datetimepicker1', 'size': 10}))
    close_time = forms.TimeField(widget=forms.TimeInput(attrs={'id': 'datetimepicker2', 'size': 10}))
    open_order = forms.TimeField(widget=forms.TimeInput(attrs={'id': 'datetimepicker3', 'size': 10}))
    close_order = forms.TimeField(widget=forms.TimeInput(attrs={'id': 'datetimepicker4', 'size': 10}))
    class Meta:
        model = Store
        fields = ('storename', 'detail', 'open_time', 'close_time', 'open_order', 'close_order', 'open_day', 'email', 'phone', 'fbpage', 'lineac', 'igac', 'address')
