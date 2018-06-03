from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from pages.models import Creation, About, Contact

# TODO: Setup admin relation
#       Wysiwig
#       error 404

def index(request):
    creations = Creation.objects.all().order_by('-created_at')
    creation_first = creations.first()
    creation_cleaned = creations.exclude(id=creation_first.id)

    return render(request, 'home.html', {
        'creation_first': creation_first,
        'creations': creation_cleaned
    })


def creation_detail(request, slug):
    creation = get_object_or_404(Creation, slug=slug)
    return render(request, 'creation_detail.html', {
        'creation_detail': creation
    })


def about(request):
    about = About.objects.all().first()
    return render(request, 'about.html', {
        'about': about,
    })


def contact(request):
    if request.method == 'POST':
        Contact.objects.create(email=request.POST.get('email'), message=request.POST.get('message'))
        return redirect('thankyou')
    return render(request, 'contact.html', {})


def thankyou(request):
    return render(request, 'thankyou.html', {})