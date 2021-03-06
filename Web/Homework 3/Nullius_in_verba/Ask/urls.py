from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'login/$', views.login, name='login'),
	url(r'signup/$', views.signup, name='signup'),
	url(r'tag/(?P<tag>[\w\-]+)/', views.tag, name='tag'),
	url(r'error/$', views.error, name='error'),
	url(r'ask/$', views.ask, name='ask'),
	url(r'hot/$', views.hot, name='hot'),
	url(r'question/(?P<id>\d+)/', views.question, name='question'),
    url(r'', views.index, name='index'),
]
