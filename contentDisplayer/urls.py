from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^getContentInfo/(\d+)$', views.content, name="content"),
	url(r'^getContentList$', views.contentList),
]
