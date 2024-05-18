# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Liste des Tables pour la base intern:
    # Kitting (Chaine, Superviseur)
    # Projets (intitulé, status)
    # Poste (intitulé, kitting_id, projet_encours = project_id)
    # Projets (intitulé, status)
    # Listing (ref_intern, ref_fourn, design, fourn, qt_stk, qt_a_sortir, poste_id, project_id, status (dispo / indispo))
    # Bon_de_sortie (poste_id, project_id, status)

class Kitting(models.Model):
    chaine = models.CharField(default="", max_length=64)
    superviseur = models.CharField(default="", max_length=64)

class Projet(models.Model):
    intitule = models.CharField(default="", max_length=64)    
    status = models.CharField(default="", max_length=64)

class Poste(models.Model):
    intitule = models.CharField(default="", max_length=64)
    kitting_id = models.ForeignKey(Kitting, on_delete=models.CASCADE)
    projet_id = models.ForeignKey(Projet, on_delete=models.CASCADE)

class Listing(models.Model): # Liste des Article selectionnés pour un Poste & Projet bien definit
    ref_intern = models.CharField(max_length=64)
    ref_fourn = models.CharField(default="", max_length=64)
    designation = models.CharField(default="", max_length=64)
    fournisseur = models.CharField(default="", max_length=64)
    qte_en_stk = models.FloatField()
    qte_a_sortir = models.FloatField()
    poste_id = models.ForeignKey(Poste, on_delete=models.CASCADE)
    projet_id = models.ForeignKey(Projet, on_delete=models.CASCADE)
    status = models.CharField(default="", max_length=64) # (dispo / indispo)

class Bon_de_sortie(models.Model):
    poste_id = models.ForeignKey(Poste, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projet, on_delete=models.CASCADE)
    status = models.CharField(default="En préparation", max_length=64) # status (En préparation, Imprimé, Envoyé)



# Liste des Tables pour la Base SAGE
    # Article
    # Article_stock
    # Affaires
    # Fournisseur

class Fournisseur(models.Model):
    nom = models.CharField(default="", max_length=64)
        

class Article(models.Model):
    ref_intern = models.CharField(max_length=64)
    ref_fourn = models.CharField(default="", max_length=64)
    designation = models.CharField(default="", max_length=64)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Art_stock(models.Model):
    ref_intern = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte = models.FloatField()