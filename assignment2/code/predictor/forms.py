#use django forms
from django import forms


#use django forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#========================================================================
## Stock Prediction Form
#========================================================================   
class StockPredictionForm(forms.Form):
    stock_symbol = forms.CharField(
        label='Stock Symbol',
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. BHP'})
    )
    months = forms.IntegerField(
        label='Months Ahead (1–6)',
        min_value=1,
        max_value=6,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g. 3'})
    )


#========================================================================
## Register and Login Forms
#========================================================================
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)