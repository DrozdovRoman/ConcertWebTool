from re import T
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {

    }
    
    template = "core/index.html"
    return render(request,template,context)