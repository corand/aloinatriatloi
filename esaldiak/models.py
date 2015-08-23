from django.db import models

# Create your models here.
class Esaldi(models.Model):
	esaldia = models.TextField()
	egilea = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.esaldia