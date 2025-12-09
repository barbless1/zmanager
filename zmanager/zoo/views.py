#Ce fichier permet de changer les pages accessibles en fonction de l'utilisateur connecté.
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Animal, Accidents, Visite, Soigneur
from django.shortcuts import render, get_object_or_404

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
    animal_count = Animal.objects.count()
    accidents = Accidents.objects.all()

    for accident in accidents:
        # Convert DateAccident (date) to datetime at midnight local time
        accident_datetime = datetime.combine(accident.DateAccident, datetime.min.time(), tzinfo=timezone.get_current_timezone())
        accident.since = timezone.now() - accident_datetime

    context = {
        'animal_count': animal_count,
        'accidents': accidents
    }

    return render(request, 'dashboard.html', context)

@login_required
def dashboard(request):
    animals = Animal.objects.all()
    context = {"animals": animals, "is_admin": request.user.is_superuser}
    return render(request, "animaux.html", context)


@login_required
def visites(request):
    visites = Visite.objects.all()
    return render(request, 'visites.html', {"visites": visites})
    


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

@login_required
def animal_edit(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, "animal_edit.html", {"animal": animal})

@login_required
def add_visite(request):
    if request.method == "POST":
        DateDerniereVisite = request.POST.get("DateDerniereVisite")
        DateDernierVaccin = request.POST.get("DateDernierVaccin")
        Pathologie = request.POST.get("Pathologie")
        DescriptionVisite = request.POST.get("DescriptionVisite")
        Animal_id = request.POST.get("Animal")
        Visite.objects.create(
            DateDerniereVisite=DateDerniereVisite,
            DateDernierVaccin=DateDernierVaccin,
            Pathologie=Pathologie,
            DescriptionVisite=DescriptionVisite,
            Animal_id=Animal_id
    )

        return redirect("/visites")

    soigneurs = Soigneur.objects.all()
    animaux = Animal.objects.all()
    return render(request, "add_visite.html", {
        "soigneurs": soigneurs,
        "animaux": animaux,
    })

@login_required
def visites_list(request):
    visites = Visite.objects.all()
    return render(request, "visites.html", {"visites": visites})
def soigneurs(request):
    soigneur = Soigneur.objects.all()
    return render(request, 'soigneurs.html', {"soigneur": soigneur})


@login_required
def soigneur_detail(request, id):
    soigneur = get_object_or_404(Soigneur, id=id)
    return render(request, 'soigneur_detail.html', {'soigneur': soigneur})

