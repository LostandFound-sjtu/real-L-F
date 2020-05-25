from django.db import models
from home.models import MyUser
# Create your models here.
from tag.models import Tag
from django.urls import reverse


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
    mail_address = models.CharField(max_length=50, default='')
    image = models.FileField(blank=True)
    identification_mark = models.TextField(help_text='Separate each item by comma',blank=True)
    secret_information = models.TextField(help_text='Separate each item by comma',blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    tmp_slug=models.CharField(max_length=30,default='')

    def save(self, *args, **kwargs):
        self.tmp_slug = self.tag.name
        super(Item, self).save(*args, **kwargs)

#   def get_url(self):
#      return reverse('lost_item', kwargs={'comment_pk': self.pk})

#   该方法返回物品的邮件地址属性，用于评论提醒功能
    def get_mail(self):
        return self.mail_address

    def __str__(self):
        return self.status

    class Meta:
        ordering = ["-update"]

    def get_contents(self):
        return self.identification_mark.split(",")

    def get_excludes(self):
        return self.secret_information.split(",")

