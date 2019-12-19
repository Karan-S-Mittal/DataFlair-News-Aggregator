from django.conf import settings
from django.db import models


# Create your models here.

# Scrape data coming from websites
# The posts will contain images, urls and titles

# model - headline(title, image, url)

# model - userprofile(user, last_scrape)

class Headline(models.Model):
	title = models.CharField(max_length=200)
	image = models.URLField(null=True, blank=True)
	url = models.TextField()

	def __str__(self):
		return self.title
