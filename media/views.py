from django.shortcuts import render, redirect, get_object_or_404
from .models import Media
from home.models import User

# Create your views here.
def index(request):
    medias = Media.objects.all()[:5]
    users = User.objects.all()

    return render(request, 'media/index.html', {'medias': medias, 'users': users})

def adicionar(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        media = Media()
        media.mediaType = request.POST['mediaType']
        media.title = request.POST['title']
        media.content = request.POST['content']
        media.url = request.POST['url']
        media.author = user
        
        if 'thumbnail' in request.FILES:
            media.thumbnail = request.FILES['thumbnail']

        if 'file' in request.FILES:
            media.file = request.FILES['file']
            
        media.save()
        return redirect('media.index')
    return render(request, 'media/add.html')

def media_detail(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    return render(request, 'media/details.html', {'media': media})

def media_type(request, type):
    users = User.objects.all()
    medias = Media.objects.filter(mediaType=type)

    return render(request, 'media/index.html', {'medias': medias, 'users': users})

def media_user(request, user_id):
    user = User.objects.get(id=user_id)
    users = User.objects.all()
    medias = Media.objects.filter(author=user)

    return render(request, 'media/index.html', {'medias': medias, 'users': users})