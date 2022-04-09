from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from scraping.models import Follower
from .utils import habr_parser

class Index(View):
    def get(self, request):
        posts = habr_parser('https://habr.com/ru/all/')
        return render(request, 'index.html', {'posts':posts})

    def post(self, request):
        email = request.POST.get('email')
        f = Follower.objects.filter(email=email)
        if f:
            return HttpResponse('Вы уже подписались')
        if email:
            f = Follower(email=email)
            f.save()
        return redirect('index')

