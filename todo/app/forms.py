from django import forms
from .models import AddTask

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ['task_name','description','duedate','duetime']

    def clean_task_name(self):
        task_name = self.cleaned_data['task_name']
        if not task_name:
            raise forms.ValidationError('Task name cannot be empty')
        return task_name 