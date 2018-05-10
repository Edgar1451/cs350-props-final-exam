# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Used for testing views.
from django.test import Client
from django.urls import reverse
from django.utils.http import urlencode


class TestTransactionViews(TestCase):
    #  load the database with relevant data
    fixtures = ['transaction-testdata.json', 'property-testdata.json']
    
    def test_lookup_success_view(self):
        #  create the client simulator
        client = Client()
        query_str = urlencode({'search_query':'offer'})
        
        url = reverse('transactions:search') + '?' + query_str
        
        #  fake a client request to url and get response object (what is sent to browser from the associated view)
        response = client.get(url)

        #  Grab the context variable known as 'results'. See transactions/views.py
        result_var = response.context['results']

        #  Verify that the number of result matches what was expected by query
        expected_count = 2
        results_count = len(result_var)
        self.assertEqual(results_count, expected_count)

    def test_lookup_failure_view(self):
        """ Test a search failure """

        #  create the client simulator
        client = Client()
        query_str = urlencode({'search_query':'lava'})
        
        url = reverse('transactions:search') + '?' + query_str
        
        #  fake a client request to url and get response object (what is sent to browser from the associated view)
        response = client.get(url)

        #  Grab the context variable known as 'results'. See transactions/views.py
        result_var = response.context['results']

        #  Verify that the number of result matches what was expected by query
        expected_count = 0
        results_count = len(result_var)
        self.assertEqual(results_count, expected_count)