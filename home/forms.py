from django import forms
from django.forms import ModelForm
from . models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['commenter', 'post', 'status']

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    first_name =  forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    class META:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



