from django import forms
from django.db import models

class OutputForm(forms.Form):
    output = forms.CharField(required=True, max_length=1000)