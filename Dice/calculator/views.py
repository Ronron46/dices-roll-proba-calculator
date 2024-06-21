from django.http import HttpResponse
from django.shortcuts import render
from calculator.forms import OutputForm
from calculator.services.dice_program.objects.DataCleaner import DataCleaner
from calculator.services.dice_program.objects.Control import Control
from calculator.services.dice_program.functions.zero_counter import zero_counter
from calculator.services.dice_program.objects.Graph import Graph
import time

def calculator(request):
    if request.method =='POST':
        time_start=time.time()
        form=OutputForm(request.POST)
        dice_list=DataCleaner(request.POST['dés'])
        time_start=time.time()
        control=Control(dice_list)
        timer=time.time() - time_start
        timer=round(timer, 4)
        count=control.res
        res_min=control.res_min
        graph=Graph(count, res_min)
        abscisse, count, less, more, total_comb = graph.data()
        return render(request,'calculator/calc.html', {'form' : form, 'count' : count, 'abs' : abscisse, 'total_comb' : total_comb, 'timer' : timer, 'less' : less, 'more' : more})
    else:
        form=OutputForm()
    return render(request, 'calculator/calc.html', {'form' : form})
# Create your views here.
