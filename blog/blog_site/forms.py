from django import forms
from api.models import BlogModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','content','image']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')