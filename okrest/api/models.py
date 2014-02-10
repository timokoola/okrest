from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Heading(models.Model):
	original = models.CharField(max_length=140)
	owner = models.ForeignKey(User, null=True)
	url = models.URLField()
	corrected = models.CharField(max_length=100)
	notes = models.TextField()
	contributor = models.CharField(max_length=30)
	timestamp = models.DateTimeField()


	# 'id', original', 'owner', 'url', 'corrected', 'notes', 'contributor', 'timestamp'