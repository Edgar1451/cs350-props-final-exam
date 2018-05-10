# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Message

class MessageListView(generic.ListView):
    """Add a way to display a list of all messages in the db in a html page."""
    model = Message
    template_name = "messenger/list.html"

class MessageCreateView(generic.CreateView):
    model = Message
    template_name = 'messenger/add.html'
    fields = ['subject', 'text', 'sender_email']
    success_url = reverse_lazy("messenger:list")


