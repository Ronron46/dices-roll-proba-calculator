from django.http import HttpResponse
from django.shortcuts import render
from calculator.forms import OutputForm
from calculator.services.dice_program.objects.DataCleaner import DataCleaner
from calculator.services.dice_program.objects.Control import Control

def calculator(request):
    if request.method =='POST':
        form=OutputForm(request.POST)
        dice_list=DataCleaner(request.POST['output'])
        control=Control(dice_list)
        count=control.res
        return render(request,'calculator/calc.html', {'form' : form, 'count' : count})
    else:
        form=OutputForm()
    return render(request, 'calculator/calc.html', {'form' : form})
# Create your views here.
