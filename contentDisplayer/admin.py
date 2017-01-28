from django.contrib import admin
from .models import Article, Tag, Section, Document, Image, Competence, CompetenceLink

# Register your models here.

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(Document)
admin.site.register(Image)
admin.site.register(Competence)
admin.site.register(CompetenceLink)
