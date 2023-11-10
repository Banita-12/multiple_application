from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def capital(request):
    return render(request,'capital.html')

def ut(request):
    return HttpResponse('<h3>It is one of the Union Territory</h3>')