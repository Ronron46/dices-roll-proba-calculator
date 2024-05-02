from django.http import HttpResponse
from django.shortcuts import render

def calculator(request):
    return render(request, 'calculator/calc.html')
# Create your views here.
