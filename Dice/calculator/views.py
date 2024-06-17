from django.http import HttpResponse
from django.shortcuts import render
from calculator.forms import OutputForm
from calculator.services.dice_program.objects.DataCleaner import DataCleaner
from calculator.services.dice_program.objects.Control import Control
from calculator.services.dice_program.functions.zero_counter import zero_counter
import time

def calculator(request):
    if request.method =='POST':
        time_start=time.time()
        form=OutputForm(request.POST)
        dice_list=DataCleaner(request.POST['output'])
        time_start=time.time()
        control=Control(dice_list)
        timer=time.time() - time_start
        timer=round(timer, 4)
        count=control.res
        lis=control.res.copy()
        res_min=control.res_min
        combi=sum(count)
        for i in range(len(count)):
            count[i]/=combi
        total_comb = zero_counter(combi)
        abscisse = []
        for i in range (len(count)):
            abscisse.append(i+res_min)
        less=[]
        for i in range(len(count)):
            if i ==0:
                less.append(count[i])
            else:
                less.append(less[i-1]+count[i])

        return render(request,'calculator/calc.html', {'form' : form, 'count' : count, 'abs' : abscisse, 'total_comb' : total_comb, 'timer' : timer, 'lis' : lis, 'less' : less})
    else:
        form=OutputForm()
    return render(request, 'calculator/calc.html', {'form' : form})
# Create your views here.
