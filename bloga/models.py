from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
import datetime

# Blogeko postak
class Post(models.Model):
    izenburua = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    edukia = RichTextField()
    etiketak = TaggableManager()
    slug = models.CharField(max_length=150, blank=True,unique=True)
    irudi_nagusia = models.ImageField()

    def save(self):
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.izenburua)
        )
        super(Post, self).save()

    def get_next(self):
        next = Post.objects.filter(data__gt=self.data)
        if next:
            return next[0]
        return False

    def get_prev(self):
        prev = Post.objects.filter(data__lt=self.data).order_by('-data')
        if prev:
            return prev[0]
        return False

    def __unicode__(self):
        return self.izenburua