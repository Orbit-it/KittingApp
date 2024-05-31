# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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

    selection_id = State_selection.objects.all()

    # End =====================================================================

    
    context = {'segment': 'index',
            "articles": list_article,
            "list_fournisseur": list_fournisseur,
            "list_projet": list_projet,
            "poste": poste,
            "listing": listing,
            'selection_id': selection_id,
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
            selection_id = State_selection.objects.update(selected_poste_id = id)
            # Effectuez des opérations avec l'objet `poste` selon vos besoins
            return JsonResponse({"status": "success", "intitule_du_poste": poste.intitule, "projet_encours": poste.projet_id.intitule})
        except Poste.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Poste not found."})
    return JsonResponse({"status": "error", "message": "Invalid request method."})

@login_required(login_url="/login/")
def get_articles(request):
        article_id = request.GET.get('ref_intern')
        qts = request.GET.get('qts')
        try:
            
            article = Article.objects.get(ref_intern=article_id)
            recup_qte = Art_stock.objects.get(ref_intern = article.id)

            if (float(recup_qte.qte) < float(qts)):
                status = "Indisponible"
            else: status = "dispo"

            article_data = {
                'fournisseur': article.fournisseur.nom,
                'designation': article.designation,
                'ref_intern': article.ref_intern,
                'ref_fourn': article.ref_fourn,
                'qte':recup_qte.qte,
                'qte_s': qts,
                'status':status
            }

            

            Listing.objects.create(ref_intern = article.ref_intern, ref_fourn = article.ref_fourn, designation = article.designation, 
                                   fournisseur = article.fournisseur.nom, qte_en_stk = recup_qte.qte, qte_a_sortir = qts, status = status,
                                   bon_de_sortie_id = 1)
            return JsonResponse({'article': article_data})
        except Article.DoesNotExist: 
            return JsonResponse({"status": "error", "message": "Article not found."})     