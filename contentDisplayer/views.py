from django.shortcuts import render
from .models import Content


# Create your views here.

def content(request, contentId):
	contentToDisplay = Content.objects.get(id=contentId)
	return render(request, 'contentDisplayer/content.html', {'contentToDisplay' : contentToDisplay})

def contentList(request):
	contents = Content.objects.all()
	return render(request, 'contentDisplayer/contentList.html', {'contents' : contents})
