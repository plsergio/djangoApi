from django.shortcuts import render
from .models import Person
from .forms import PersonForm

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

def persons_new(request):
    form = PersonForm(request.POST, None)
    return render(request, 'person_form.html',{'form':form})