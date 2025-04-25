from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def create(request):
    if request.method == 'POST':
        if(request.POST['senha'] == request.POST['confirmar_senha']):
            try:
                User.objects.create(name=request.POST['nome'], email=request.POST['email'], password=request.POST['senha'])
                return redirect('home.login')
            except:
                return render(request, 'home/register.html')
        else:
            return render(request, 'home/register.html')
    return render(request, 'home/register.html')

def login(request):
   if request.method == 'POST':
       user = User.objects.filter(email=request.POST['email'], password=request.POST['senha'])
       if user:
           request.session['user_name'] = user[0].name
           request.session['user_id'] = user[0].id
           return redirect('home.index')
       else:
           return render(request, 'home/login.html')
   return render(request, 'home/login.html')

def logout(request):
    request.session.flush()
    return redirect('home.index')