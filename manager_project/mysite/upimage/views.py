from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def index(req):
    if req.method == 'GET':
        return render(req, 'upimage/index.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.all(), # ここを追加

        })

    elif req.method == 'POST':                                                     
        form = PhotoForm(req.POST, req.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        photo = Photo()
        photo.image = form.cleaned_data['image']
        photo.save()

        return redirect('/upimage/')
