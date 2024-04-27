from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def calculate(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    op=request.GET["opt"]
    con_dict={}
    if op=="add":
        con_dict["res"]=x+y
    elif op=="sub":
        con_dict["res"]=x-y
    elif op=="mul":
        con_dict["res"]=x*y
    else:
        con_dict["res"]=x/y
    return render(request,'result.html',context=con_dict)