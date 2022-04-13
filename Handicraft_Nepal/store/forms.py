from attr import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,required=True)
    last_name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(max_length=250,help_text='eg. youremail@gmail.com')

    class Meta:
        model=User
        fields=('first_name','last_name','username','password1','password2','email')

class ContactForm(forms.Form):
    Subject=forms.CharField(max_length=50,required=True)
    Name=forms.CharField(max_length=50,required=True)
    Email=forms.EmailField(max_length=50,required=True)
    Message=forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
        help_text="Write your message here!!"
        )