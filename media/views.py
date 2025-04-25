from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Oi, mundo")
    #return render(request, 'schedule/index.html')