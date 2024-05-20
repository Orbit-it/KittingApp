# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *


@login_required(login_url="/login/")
def index(request):

     # Objects from Sage =======================================================
    list_article = Article.objects.all()
    list_fournisseur = Fournisseur.objects.all()
    list_projet = Projet.objects.all()
    # End =====================================================================

    # Objects from internal DB ================================================
    poste = Poste.objects.all()
    listing = Listing.objects.all()

    # End =====================================================================

    
    context = {'segment': 'index',
            "list_article": list_article,
            "list_fournisseur": list_fournisseur,
            "list_projet": list_projet,
            "poste": poste,
            "listing": listing,
               }
    

   

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):

    context = {}


    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def selected_poste(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            poste = Poste.objects.get(id=id)
            # Effectuez des opérations avec l'objet `poste` selon vos besoins
            return JsonResponse({"status": "success", "intitule_du_poste": poste.intitule, "projet_encours": poste.projet_id.intitule})
        except Poste.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Poste not found."})
    return JsonResponse({"status": "error", "message": "Invalid request method."})