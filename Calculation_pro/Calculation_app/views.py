from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

# Here i and j is equal to None not mandatory to write.
# i=None
# j=None

def input(request):
    return render(request,'add.html')

def new_output(request):
    va11=request.GET['t1']
    val2=request.GET['t2']

    global i
    global j
    i=int(va11)
    j=int(val2)

    z=request.GET['but']

    if z=='Add':
        return redirect(add)
    if z=='Sub':
        return redirect(sub)
    if z=='Mul':
        return redirect(mul)
    if z=='Div':
        return redirect(div)

def add(request):
    k=i+j
    data="The addition of",i,"and",j,"is:",k
    return HttpResponse(data)

def sub(request):
    k=i-j
    data="The subtraction of",i,"and",j,"is :",k
    return HttpResponse(data)

def mul(request):
    k=i*j
    data = "The multiplication of",i, "and", j, "is :", k
    return HttpResponse(data)

def div(request):
    k=i/j
    data = "The division of", i, "and", j, "is :", k
    return HttpResponse(data)
