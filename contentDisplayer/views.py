from django.shortcuts import render
from .models import Article, Section, Document, Image, Tag, Competence, CompetenceLink
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.


def articleAssociatedToTag(tag):
	articles = tag.article_set.all()
	return articles

def getChildArticles(article):
	articles = article.article_set.all()
	return articles

def tagAssociatedToArticle(article):
	tags = article.tags.all()
	return tags

def content(request, contentId):
	article = Article.objects.get(id=contentId)
	sections = Section.objects.filter(parentArticle__id=contentId).order_by('order')
	images = Image.objects.filter(parentArticle__id=contentId)
	imageCount = len(images)
	documents = Document.objects.filter(parentArticle__id=contentId)
	docCount = len(documents)
	tags = tagAssociatedToArticle(article).order_by('name')

	ufCompetences = article.competencesForUF.all().order_by('targetUF__title')
	
	return render(request, 'contentDisplayer/content.html', {'article' : article, 'sections' : sections, 'images' : images, 'imageCount' : imageCount, 'documents' : documents, 'docCount' : docCount, 'tags' : tags, 'ufCompetences' : ufCompetences})

def contentList(request):
	articles = Article.objects.all()
	return render(request, 'contentDisplayer/contentList.html', {'nodes' : articles})

def articleListFromTag(request, tagId):
	tag = Tag.objects.get(id=tagId)
	relatedArticles = articleAssociatedToTag(tag)

	return render(request, 'contentDisplayer/articleListFromTag.html', {'tag' : tag, 'articles' : relatedArticles})
