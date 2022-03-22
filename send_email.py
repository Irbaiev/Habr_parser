import os
import sys
from datetime import datetime

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import django
django.setup()

from django.core.mail import EmailMultiAlternatives
from core.settings import EMAIL_HOST_USER
from scraping.models import Follower
from habr import habr_parsing

posts = habr_parsing()
emails = Follower.objects.all()
subject = 'Посты на сегодня {datetime.now()}'
from_email = EMAIL_HOST_USER
text_content = 'Посты на сегодня'
html_content = ''
for email in emails:
    for post in posts:
        html_content += f'''<a href = "{ post.get('profile') }"<h5>{ post.get('user') }</h5></a> 
              <h3 class="card-title">{ post.get('title') }</h3> 
              <a href="{ post.get('urls') }" class="btn btn-primary">Читать далее</a><br>'''
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send() 