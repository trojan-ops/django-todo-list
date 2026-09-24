from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']

class UpdateTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
