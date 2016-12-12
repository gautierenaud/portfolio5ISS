from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Content(models.Model):
	title = models.CharField(max_length=200)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	parentSubject = models.ForeignKey('self', null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	challenges = models.TextField(null=True, blank=True)
	acquiredCompetences = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title
