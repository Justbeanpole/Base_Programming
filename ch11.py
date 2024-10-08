import requests as rq
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%89%B4%EC%A7%84%EC%8A%A4"
res = rq.get(url)
html = res.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

word = soup.select('.news_tit')
for i in word:
    print(i.text)
    # print(i.attrs['href'])