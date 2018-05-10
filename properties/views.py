# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Property


# Show the all the properties in the db.

class PropertyListView(generic.ListView):
    model = Property
    template_name = "properties/list.html"


class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = "properties/detail.html"


class PropertyCreateView(generic.CreateView):
    model = Property  # what type of object we are creating?
    template_name = "properties/create.html"  # the page to display the form.
    fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
    success_url = reverse_lazy('properties:list')


class PropertyUpdateView(generic.UpdateView):
    model = Property  # what type of object we are editing?
    template_name = "properties/edit.html"  # the page to display the form.
    fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
    success_url = reverse_lazy('properties:list')
