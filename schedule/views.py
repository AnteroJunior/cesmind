from django.shortcuts import render
from .models import Schedule
# Create your views here.
def index(request):
    return render(request, 'schedule/index.html')

def agendar(request):
    if request.method == 'POST':
        agendamento = Schedule(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            matricula=request.POST['matricula'],
            course=request.POST['course'],
            period=request.POST['period'],
            reason=request.POST['reason'],
            availability=request.POST['availability']
        )
        agendamento.save()
        return render(request, 'schedule/index.html')
    return render(request, 'schedule/index.html')