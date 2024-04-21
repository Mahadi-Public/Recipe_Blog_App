from typing import Any
from django import forms
from recipe.models import Newsletter,Contact

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        widgets = {
            'email' : forms.TextInput(attrs={'placeholder' : 'Subscribe to newsletter'})
        }
    
    def save(self, commit=True):
        submit = super().save(commit=False)
        submit.is_submit = True
        if commit:
            submit.save()
        return submit    
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'cols': '30', 'rows': '10'}),
        }