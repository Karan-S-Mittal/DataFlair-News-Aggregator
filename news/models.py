from django.db import models


# Create your models here.

# Scrape data coming from websites
# The posts will contain images, urls and titles

class Headline(models.Model):
	title = models.CharField(max_length=300)
	image = models.URLField(max_length=1000, blank=True)
	url = models.URLField(max_length=500)

	def __str__(self):
		return self.title
