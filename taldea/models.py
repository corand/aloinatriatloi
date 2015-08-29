from django.db import models

# Create your models here.
class Harremana(models.Model):
	izena = models.CharField(max_length=150)
	emaila = models.EmailField()
	textua = models.TextField()
	data = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.id) + ' ' + self.izena

