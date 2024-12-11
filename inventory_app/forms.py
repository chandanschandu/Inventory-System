from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_type', 'purchase_date', 'stock_available']

    # Customize the date input widget
    purchase_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'})
    )