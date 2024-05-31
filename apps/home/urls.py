# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('selected_poste', views.selected_poste, name='selected_poste'),
    path('get_articles/', views.get_articles, name='get_articles'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
