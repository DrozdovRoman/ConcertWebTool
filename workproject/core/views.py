from django.shortcuts import redirect, render
from .models import Concert
from .forms import ConcertForm
from django.urls import reverse

# Create your views here.

def home(request):
    context = {

    }
    
    template = "core/index.html"
    return render(request,template,context)

def concert(request):
    success = False 
    if request.method == 'POST':
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    context = {
        "list_concert" : Concert.objects.all().order_by("id"),
        "form" : ConcertForm,
        "success" : success
    }
    
    template = "core/concert.html"
    return render(request,template,context)

def update_page(request,pk):
    success_update = False
    get_concert = Concert.objects.get(pk = pk)
    if request.method == 'POST':
        form = ConcertForm(request.POST, instance = get_concert)
        if form.is_valid():
            form.save()
            success_update = True

    context = {
        'get_concert' : get_concert,
        'update': True,
        'form':ConcertForm(instance = get_concert),
        'success_update':success_update
    }
    
    template = "core/concert.html"
    return render(request,template,context)

def delete_page(request,pk):
    get_concert = Concert.objects.get(pk = pk)
    get_concert.delete()
    return redirect(reverse('concert'))