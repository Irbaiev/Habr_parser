import imp
from django.shortcuts import render
import requests
from .utils import habr_parser

def home(request):
    posts = habr_parser('https://habr.com/ru/all/page1/')
    return render(request, 'index.html', {'posts':posts})

