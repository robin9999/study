#video/urls.py
from django.conf.urls import url, include
from . import views

app_name='video' # app_name 설정
urlpatterns =[
	url(r'^$',views.video_list,name='list'),
	#아래 코드 추가하기
	url(r'^new$', views.video_new, name='new'),
	url(r'^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
]
