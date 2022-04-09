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

posts =[]

link = 'https://habr.com/ru/all/'

u = 1

def habr_parser(link):
    for u in range(5):
        res = requests.get(f'{link}page{u}', headers=choice(headers))
        if res.status_code == 200:
                soup = BS(res.content, 'html.parser')
                article = soup.find('div', class_ = 'tm-articles-list')
                div = article.find_all('div', class_ = 'tm-article-snippet')
                for i in div:
                    user = i.find('a', class_ = 'tm-user-info__username').text.strip()
                    profile = 'https://habr.com' + i.a['href']
                    urls = 'https://habr.com' + i.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').a['href']
                    title = i.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').text.strip()
                    # desc = i.find('div', class_ = 'article-formatted-body article-formatted-body_version-2').find_next('p')
                    posts.append({'user':user, 'profile':profile, 'urls':urls, 'title': title})
                    # , 'desc':desc})
                    u =+ 1
    return posts

    conn = sqlite3.connect('posts.db')

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO posts VALUES (?,?,?,?)", posts)

    conn.commit()
