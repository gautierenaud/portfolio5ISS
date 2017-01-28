from __future__ import unicode_literals
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)
	taggedArticles = models.ManyToManyField('Article', blank=True)

	def __str__(self):
		return self.name

class Article(MPTTModel):
	title = models.CharField(max_length=200)
	tags = models.ManyToManyField(Tag, blank=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	isUF = models.BooleanField(default=False)

	class MPTTMeta:
		order_insertion_by = ['title']

	def __str__(self):
		return self.title

class Section(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(null=True, blank=True)
	order = models.IntegerField(default=0, null=False, blank=True)
	parentArticle = models.ForeignKey(Article, null=True, blank=False)

	def __str__(self):
		return self.parentArticle.title + " - " + self.title

class Document(models.Model):
	title = models.TextField(null=False, blank=False)
	docName = models.TextField(null=False, blank=False)
	parentArticle = models.ForeignKey(Article, null=True, blank=False)

	def __str__(self):
		return self.parentArticle.title + " - " + self.title

class Image(models.Model):	
	title = models.TextField(null=False, blank=False)
	imageName = models.TextField(null=False, blank=False)
	parentArticle = models.ForeignKey(Article, null=True, blank=False)

	def __str__(self):
		return self.parentArticle.title + " - " + self.title

class Competence(models.Model):
	parentUF = models.ForeignKey(Article, related_name="competencesForUF")
	targetUF = models.ForeignKey(Article, related_name="competencesForSubUF")
	title = models.TextField(null=False, blank=False)
	level = models.IntegerField(default=3, null=False, blank=True)
	expectedLevel = models.IntegerField(default=3, null=False, blank=True)

	def __str__(self):
		return self.targetUF.title + " - " + self.title

class CompetenceLink(models.Model):
	competence = models.ForeignKey(Competence, related_name="fulfillingArticles")
	linkedArticle = models.ForeignKey(Article, related_name="acquiredCompetences")

	def __str__(self):
		return self.linkedArticle.title + " - " + self.competence.title
