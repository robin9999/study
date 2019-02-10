##parser.py

import requests
from bs4 import BeautifulSoup
#import json
import os

## python 파일 위치
#BASE_DIR=os.path.dirname(os.path.abspath(__file__))

#python 이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에서 현재 프로젝트의 settings.py파일 경로를 등록.

os.environ.setdefault("DJANGO_SETTINGS_MODULE","websaver.settings")
## 이제 장고를 가져과 장고 프로젝트를 사용할 수 있또록 환경 만듦.
import django
django.setup()
## Blog data를 import 해옴
from parsed_data.models import BlogData


def parse_blog():
	req = requests.get('https://beomi.github.io/beomi.github.io_old/')
	html = req.text
	soup = BeautifulSoup(html,'html.parser')
	my_titles = soup.select(
		'h3 > a'
		)
	data ={}
	for title in my_titles:
		data[title.text] = title.get('href')
	return data

#이 명령어는 이 파일이 import 가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 함.
if __name__=='__main__':
	blog_data_dict = parse_blog()
	for t,l in blog_data_dict.items():
		BlogData(title=t, link=l).save()
	
#with open(os.path.join(BASE_DIR,'result.json'),'w+') as json_file:
#	json.dump(data,json_file)


