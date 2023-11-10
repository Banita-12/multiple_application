from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def o(request):
    return render(request,'odisha.html')

def od(request):
    return HttpResponse('<h1>It locates eastern part of India.</h1>')