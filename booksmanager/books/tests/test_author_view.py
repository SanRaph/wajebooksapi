import json

import requests
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Author

class TestAuthorViewSet():

    def setUp(self):
        self.client = APIClient()
        local_host_url = 'http://127.0.0.1:8000/api/authors' # if needed


         # create object using model
        author = Author.objects.create(first_name='Raphael', last_name='Sani')


def test_create_author(self):
    data = {"first_name": "Janna", "last_name": "Marrie"}

    # creating author via api
    response = self.client.post(reverse('author-list'), data=data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


def test_get_authors(self):

    # getting authors via api
    response = self.client.get(reverse('author-list'))
    self.assertEqual(response.status_code, status.HTTP_200_CREATED)
    