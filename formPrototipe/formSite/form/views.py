from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   
    return HttpResponse("<h1> Hello<h1>")

def results(request):
    #Return results
    pass
