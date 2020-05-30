from django.db import models
from home.models import MyUser
# Create your models here.
from tag.models import Tag
from django.urls import reverse


class Item(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='创建者')
    name = models.CharField(max_length=50, verbose_name='名称')
    CATEGORY_CHOICES = (
        ('F', '拾到物品'),
        ('L', '丢失物品'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="Found Item",verbose_name='类别')
    location = models.CharField(max_length=50, verbose_name='地点')
    phone_number = models.CharField(max_length=16, verbose_name='手机号码')
    mail_address = models.CharField(max_length=50, default='', verbose_name='Email地址')
    image = models.FileField(blank=True, verbose_name='图片')
    identification_mark = models.TextField(blank=True, verbose_name='具体信息')
    secret_information = models.TextField(help_text='Separate each item by comma', blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签')

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
        return self.name

    class Meta:
        ordering = ["-update"]

    def get_contents(self):
        return self.identification_mark.split(",")
