import requests
from bs4 import BeautifulSoup

# 특정 url에 접속하는 요청(request) 객체 생성
request = requests.get('https://namu.wiki/w/%EB%B9%84%EB%91%98%EA%B8%B0#toc')

#접속한 이후 웹사이트 추출
html = request.text

#html 소스코드를 파이썬 객체로 변환.'

soup = BeautifulSoup(html,'html.parser')

my_titles = soup.select(
   'body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > p'
    )
# my_titles는 list 객체
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))
    