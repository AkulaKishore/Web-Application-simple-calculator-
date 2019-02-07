from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.template import loader

# Create your views here.

def index(request):
    answer = ""
    if request.GET.get('add'):
        input1 = int(request.GET['input_1'])
        input2 = int(request.GET['input_2'])
        answer = str( input1 + input2)
    if request.GET.get('multiply'):
        input1 = int(request.GET['input_1'])
        input2 = int(request.GET['input_2'])
        answer = str(input1 * input2)

    if request.GET.get('subtract'):
         input1 = int(request.GET['input_1'])
         input2 = int(request.GET['input_2'])
         answer = str(input1 - input2)
    if request.GET.get('divide'):
         input1 = int(request.GET['input_1'])
         input2 = int(request.GET['input_2'])
         if input2 ==0:
             answer = 'not valid'
         else:
             answer = str(input1/input2)

        
    return render(request,"application/index.html",{'answer':answer,})

    
