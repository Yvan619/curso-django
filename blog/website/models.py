from django.db import models


class Post(models.Model):
	tittle = models.CharField(max_length=100)
	sub_tittle = models.CharField(max_length=200)
	content = models.TextField()
