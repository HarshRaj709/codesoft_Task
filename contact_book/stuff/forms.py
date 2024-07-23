from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if Contact.objects.filter(name=name).exists():
            raise forms.ValidationError('Name already registered')
        return name
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    
