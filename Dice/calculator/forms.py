from django import forms
from django.db import models

class OutputForm(forms.Form):
    dés = forms.CharField(required=True, max_length=1000)