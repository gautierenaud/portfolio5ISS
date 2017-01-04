from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=50)
	taggedArticles = models.ManyToManyField(Article, blank=True, null=True)

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=200)
	tags = models.ManyToManyField(Tag, blank=True, null=True)
	parentSubject = models.ForeignKey('self', null=True, blank=True)

	def __str__(self):
		return self.title

class Section(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(null=True, blank=True)
	order = models.IntegerField(default=0, null=False, blank=True)
	parentArticle = models.ForeignKey(Article, null=True, blank=False)

	def __str__(self):
		return self.title

class Document(models.Model):
	title = models.TextField(null=False, blank=False)
	docName = models.TextField(null=False, blank=False)
	parentArticle = models.ForeignKey(Article, null=True, blank=False)

	def __str__(self):
		return self.title

class Image(models.Model):	
	title = models.TextField(null=False, blank=False)
	imageName = models.TextField(null=False, blank=False)
	parentArticle = models.ForeignKey(Article, null=True, blank=False)

	def __str__(self):
		return self.title


