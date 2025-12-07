#Ce fichier permet de changer les pages accessibles en fonction de l'utilisateur connecté.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Animal

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def accueil(request):
    animals = Animal.objects.all()
    return render(request, 'dashboard.html'), {"animals": animals}

@login_required
def dashboard(request):
    animals = Animal.objects.all()
    return render(request, 'animaux.html', {"animals": animals})


@login_required
def add_animal(request):
    if request.method == "POST":
        Animal.objects.create(
            name=request.POST['name'],
            species=request.POST['species'],
            age=request.POST['age']
        )
        return redirect('dashboard')
    return render(request, 'animal_form.html')

@login_required
def edit_animal(request, id):
    animal = Animal.objects.get(id=id)
    if request.method == "POST":
        animal.name = request.POST['name']
        animal.species = request.POST['species']
        animal.age = request.POST['age']
        animal.save()
        return redirect('dashboard')
    return render(request, 'animal_form.html', {"animal": animal})

@login_required
def delete_animal(request, id):
    Animal.objects.get(id=id).delete()
    return redirect('dashboard')