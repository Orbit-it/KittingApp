# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Poste)
admin.site.register(Projet)
admin.site.register(Kitting)
admin.site.register(Article)
admin.site.register(Art_stock)
admin.site.register(Fournisseur)
