from django.db import models
from home.models import MyUser
# Create your models here.
from tag.models import Tag

class Item(models.Model):
    status = models.CharField(max_length=50)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    CATEGORY_CHOICES = (
        ('F', 'Found Item'),
        ('L', 'Lost Item'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="Found Item")
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    image = models.FileField()
    identification_mark = models.TextField(help_text='Separate each item by comma')
    secret_information = models.TextField(help_text='Separate each item by comma')
    # 对tag的类进行具体化，暂时分为三类
    # 这个tag的动态化貌似不太好使实现emm
    #TAG_CHOICES = (
     #   ('0', 'keys'),
      #  ('1', 'cards'),
       # ('2', 'books')
    #)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    tmp_slug=models.CharField(max_length=30,default='')

    def save(self,*args,**kwargs):
        self.tmp_slug=self.tag.slug
        super(Item,self).save(*args,**kwargs)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ["-update"]

    def get_contents(self):
        return self.identification_mark.split(",")

    def get_excludes(self):
        return self.secret_information.split(",")
