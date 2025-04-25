from django.shortcuts import render, redirect
from schedule.models import Schedule
from home.models import User

# Create your views here.
def index(request):
    schedules = Schedule.objects.all()
    notAssumed = schedules.filter(professional__isnull=True)
    assumed = schedules.filter(professional__isnull=False, professional__id=request.session['user_id'])
    return render(request, 'dashboard/index.html', {'notAssumed': notAssumed, 'assumed': assumed})

def assume(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    user = User.objects.get(id=request.session['user_id'])
    schedule.professional = user
    schedule.save()
    return redirect('dashboard.index')