from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def create(request):
    return render(request, 'home/register.html')

#def login(request):
 #   return render(request, 'oi')