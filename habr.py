import json
from random import choice
import sqlite3
import requests
from bs4 import BeautifulSoup as BS




headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]

posts = []

def habr_parsing():

    url = 'https://habr.com/ru/all/'
    res = requests.get(url, headers=choice(headers))
    pagination = len(BS(res.content, 'html.parser').find(
        'div', class_='tm-pagination').find_all('a'))
    for u in range(pagination):
        url = f'https://habr.com/ru/all/{u}/'
        if res.status_code == 200:
            soup = BS(res.content, 'html.parser')
            article =soup.find('article',class_='tm-articles-list__item')
            div = article.find_all_next('div',class_='tm-article-snippet')
            for i in div:
                title = i.find('h2',class_='tm-article-snippet__title tm-article-snippet__title_h2').text.strip()
                user = i.find('a', class_ = 'tm-user-info__username').text.strip()
                url = 'https://habr.com' + i.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').a['href']
                profile = 'https://habr.com' + i.a['href']
                # image = i.find('img', class_='tm-article-snippet__lead-image').a['src']
                description = i.find('div', class_='article-formatted-body article-formatted-body_version-2')
                views = i.find('span', class_='tm-icon-counter tm-data-icons__item')
                comm = i.find('div',class_='tm-article-comments-counter-link tm-data-icons__item')
                posts.append({'title':title,'user':user,  'url':url,'profile':profile,
                            'views':views,'comm':comm,'description':description})
    return posts
    # conn = sqlite3.connect('posts.db')

    # cursor = conn.cursor()

    # cursor.executemany("INSERT INTO posts VALUES (?,?,?,?)", posts)

    # conn.commit()

