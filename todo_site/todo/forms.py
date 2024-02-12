from django import forms
from .models import Todo, Login, Homework_Login

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class LoginForms(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class Home_Login_Forms(forms.ModelForm):
    class Meta:
        model = Homework_Login
        fields = "__all__"

