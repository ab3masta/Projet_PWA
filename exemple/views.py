from django.shortcuts import render,get_object_or_404
from .models import Exemple

def home(request):
    exemple = Exemple.objects.all()
    return render(request , 'home.html', {'posts':exemple} )

def show(request, id):
    exemple = get_object_or_404(Exemple,pk=id)
    return render(request, 'show.html', {'id':exemple})    
