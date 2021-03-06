from django.forms import ModelForm

from todolist.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'important']
