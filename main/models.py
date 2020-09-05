from django.db import models


class urlModel(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=255)
	slug = models.CharField(max_length=255, null=True)
	clicks = models.IntegerField(null=True)

	def clicked(self):
		self.clicks +=1
		self.save()

	def __str__(self):
		return self.name



