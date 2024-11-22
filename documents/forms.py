from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')

from django.core.exceptions import ValidationError

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.pdf', '.docx', '.txt')):
            raise ValidationError('Only .pdf, .docx, or .txt files are allowed.')
        return file
