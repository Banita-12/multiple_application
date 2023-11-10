from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def s(request):
    return HttpResponse('Karnataka is a southern state of India')
def B(request):
    return render(request,'bangalore.html')