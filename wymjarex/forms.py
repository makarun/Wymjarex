from django import forms

from .models import Wpis

class WpisForm(forms.ModelForm):

    class Meta:
        model = Wpis
        fields = ('weight', 'belt', 'waist','created_date')