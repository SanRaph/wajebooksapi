import json

import requests
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Author, Book

class TestAuthorViewSet():

    def setUp(self):
        self.client = APIClient()
        local_host_url = 'http://127.0.0.1:8000/api/authors' # if needed


         # create object using model
        author_1 = Author.objects.create(first_name='Raphael', last_name='Sani')
        author_2 = Author.objects.create(first_name='Felicia', last_name='Chisom')
        author_3 = Author.objects.create(first_name='Dan', last_name='Brown')

        Book.objects.create(name='Fang on the moon', isbn='53535355', author=author_1)
        Book.objects.create(name='Skipping the rope', isbn='5353566', author=author_2)
        Book.objects.create(name='Angels and Demons', isbn='77735355', author=author_3)


def test_create_a_book(self):

    data = {"name": "Fan Fare", "isbn": "737474", "author": 4}

    response = self.client.post(reverse('book-list'), data=data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


def test_get_books(self):
    response = self.client.get(reverse('book-list'))
    self.assertEqual(response.status_code, status.HTTP_200_CREATED)