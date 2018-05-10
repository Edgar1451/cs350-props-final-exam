# transactions/forms.py

from django import forms
from django.forms import Form

class TransactionLookupForm(Form):
    search_query = forms.CharField(widget=forms.TextInput, label="Search Transactions")

