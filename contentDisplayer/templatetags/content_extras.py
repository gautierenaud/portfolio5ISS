from django import template

register = template.Library()

@register.filter(name='lvlTag')
def lvlTag(lvl):
	tag = "don't try to break me!"
	if lvl == 1:
		tag = "1- application level : follow instructions"
	elif lvl == 2:
		tag = "2- analyse level : optimise the solution"
	elif lvl == 3:
		tag = "3- master level : define specifications or conceive programs"
	elif lvl == 4:
		tag = "4- expert level : define orientation or strategies"
	return tag

# look for the uf where I acquired the competence
@register.filter(name="acquiredUF")
def acquiredUF(competence):
	articleList = [competence.targetUF]

	# retrieve the external articles possibly linked to the competence
	for competenceLink in competence.fulfillingArticles.all():
		if not competenceLink.linkedArticle in articleList:
			articleList.append(competenceLink.linkedArticle)
	
	return articleList

# look for the competences I acquired in an UF
@register.filter(name="acquiredCompetences")
def acquiredCompetences(article):
	competenceList = [competence for competence in article.competencesForSubUF.all()]

	for competenceLink in article.acquiredCompetences.all().order_by("competence__targetUF__title"):
		if not competenceLink.competence in competenceList:
			competenceList.append(competenceLink.competence)

	return competenceList

@register.filter(name="getAllTags")
def getAllTags(article):
	return article.tags.all().order_by("name")
