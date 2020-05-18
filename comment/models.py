from django.db import models
from item.models import Item
from home.models import MyUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import threading
# Create your models here.


class SendMail(threading.Thread):
    def __init__(self, subject, text, email, fail_silently=False):
        self.subject = subject
        self.text = text
        self.email = email
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject,
            '您收到的新评论： /n',
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=self.fail_silently,
            html_message=self.text
        )


class ItemComment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, default=0)
    object_id = models.PositiveIntegerField(default=0)
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(default=0)
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, related_name="comments", on_delete=models.DO_NOTHING, default=0)

    root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.DO_NOTHING)
    reply_to = models.ForeignKey(MyUser, related_name="replies", null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['comment_time']

    def send_mail(self):
        if self.parent is None:
            # 评论我的item
            subject = 'Lost&Found 失物提醒邮件'
            email = self.content_object.get_mail()
            # print('email ok')
        else:
            # 回复评论
            # print('nmd,wsm')
            return
            
        if email != '':
            context = {}
            context['comment_text'] = self.text
            # context['url'] = self.content_object.get_url()
            text = render(None, 'comment/send_mail.html', context).content.decode('utf-8')
            send_mail = SendMail(subject, text, email)
            send_mail.start()




