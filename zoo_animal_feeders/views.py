from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import AnimalType, Animal, Schedule
from .forms import TypeForm, AnimalForm, ScheduleForm

# Create your views here.

def index(request):
    """Renders Home Page"""
    return render(request, 'zoo_animal_feeders/index.html')

def animal_types(request):
    """Show all animal types"""
    animal_types = AnimalType.objects.order_by('date_added')
    context = {'animal_types': animal_types}
    return render(request, 'zoo_animal_feeders/animal_types.html', context)

def animal_type(request, animal_type_id):
    """Shows a single animal type and all of the animals associated"""
    animal_type = AnimalType.objects.get(id=animal_type_id)
    animals = animal_type.animals_set.order_by('-date_added')
    context = {'animal_type':animal_type, 'animals':animals}
    return render(request, 'zoo_animal_feeders/animal_type.html', context)

def new_animal_type(request):
    """Add new animal type"""
    if request.method != 'POST':
        #Nothing submitted, blank form
        form = TypeForm()
    else:
        #POST submitted, gives data
        form = TypeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('zoo_animal_feeders:animal_types'))

    context = {'form': form}
    return render(request, 'zoo_animal_feeders/new_animal_type.html', context)

def new_animal(request, animal_type_id):
    """Add a new animal to an animal type"""
    animal_type = AnimalType.objects.get(id=animal_type_id)

    if request.method != 'POST':
        #create a blank form
        form = AnimalForm()
    else:
        #POST data submitted
        form = AnimalForm(data=request.POST)
        if form.is_valid():
            new_animal = form.save(commit=False)
            new_animal.animal_type = animal_type
            new_animal.save()
            return HttpResponseRedirect(reverse('zoo_animal_feeders:animal_type', args=[animal_type_id]))
    
    context = {'animal_type':animal_type, 'form':form}
    return render(request, 'zoo_animal_feeders/new_animal.html', context)

def edit_animal(request, animal_id):
    """edit existing animal"""
    animal = Animal.objects.get(id=animal_id)
    animal_type = animal.animal_type

    if request.method != 'POST':
        #prefill form with current animal name
        form = AnimalForm(instance=animal)
    else:
        #process data
        form = AnimalForm(instance=animal, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('zoo_animal_feeders:animal_type', args=[animal_type_id]))

    context = {'animal':animal, 'animal_type':animal_type, 'form':form}
    return render(request, 'zoo_animal_feeders/edit_animal.html', context)

def new_schedule(request, animal_id):
    """add a new schedule for the animal"""
    animal = Animal.objects.get(id=animal_id)
    animal_type = animal.animal_type

    if request.method != 'POST':
        #create 3 different checkboxes for the meals and if they check it, add that meal to their schedule
        form = ScheduleForm()
    else:
        #POST data submitted
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            new_schedule = form.save(commit=False)
            new_schedule.animal = animal
            new_schedule.save()
            return HttpResponseRedirect(reverse('zoo_animal_feeders:animal', args=[animal_id]))

def edit_schedule(request, schedule_id):
    """edit an existing animals schedule"""
    schedule = Schedule.objects.get(id=schedule_id)
    animal = schedule.animal

    if request.method != 'POST':
        #prefill with current schedule
        form = ScheduleForm(instance=schedule)
    else:
        form = ScheduleForm(instance=schedule, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('zoo_animal_feeders:animal', args=[animal_id]))

