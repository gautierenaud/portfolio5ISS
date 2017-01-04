from django.shortcuts import render
from .models import Article, Section, Document, Image
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.

def content(request, contentId):
	contentToDisplay = Article.objects.get(id=contentId)
	sections = Section.objects.filter(parentArticle__id=contentId).order_by('order')
	images = Image.objects.filter(parentArticle__id=contentId)
	imageCount = len(images)
	documents = Document.objects.filter(parentArticle__id=contentId)
	docCount = len(documents)
	
	return render(request, 'contentDisplayer/content.html', {'contentToDisplay' : contentToDisplay, 'sections' : sections, 'images' : images, 'imageCount' : imageCount, 'documents' : documents, 'docCount' : docCount})

def contentList(request):
	contents = Article.objects.all()
	return render(request, 'contentDisplayer/contentList.html', {'contents' : contents})
