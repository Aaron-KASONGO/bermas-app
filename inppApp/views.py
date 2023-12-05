from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Site, SousReseaux
import subprocess

# Create your views here.
@login_required(login_url='/admin/login')
def home(request):
    sites = Site.objects.all()
    return render(request, "inppApp/home.html", {'sites': sites})

@login_required(login_url='/admin/login')
def sous_reseaux(request, id):
    site = get_object_or_404(Site, pk=id)
    s_reseaux = site.sousreseaux_set.all()
    return render(request, "inppApp/sous_reseaux.html", {'sous_reseaux': s_reseaux})

@login_required(login_url='/admin/login')
def equipment(request, id):
    sous_reseau = get_object_or_404(SousReseaux, pk=id)
    equipments = sous_reseau.equipement_set.all()
    return render(request, "inppApp/equipment.html", {'equipments': equipments})

@login_required(login_url='/admin/login')
def open_putty(request, ip):
    subprocess.run(["putty", "open", str(ip)])
    return render(request, "inppApp/success.html")