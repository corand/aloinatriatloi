from django.db import models
from ckeditor.fields import RichTextField
from geoposition.fields import GeopositionField
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

class Gertaera(models.Model):
    izena = models.CharField(max_length=100)
    textua = RichTextField()
    kokapena = GeopositionField()
    helbidea = models.CharField(max_length=100)
    ordua = models.DateTimeField(auto_now_add=False)
    weba = models.URLField()
    slug = models.CharField(max_length=150, blank=True,unique=True)
    mota = models.ForeignKey('GertaeraMota')

    def save(self):
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.izena)
        )
        super(Gertaera, self).save()

    def __unicode__(self):
        return self.izena + ' ' + str(self.ordua)


class GertaeraMota(models.Model):
    izena = models.CharField(max_length=100)
    irudia = models.ImageField()

    def __unicode__(self):
        return self.izena