from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, default='')

    def save(self,*args,**kwargs):
            self.slug = slugify(self.name)
            super(Tag, self).save(*args, **kwargs)
    def __str__(self):
        return self.name