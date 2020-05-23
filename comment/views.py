from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import ItemComment
from .forms import CommentForm
from django.utils.timezone import localtime


def update_comment(request):
    comment_form = CommentForm(request.POST, user=request.user)
    data = {}

    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = ItemComment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']
        if parent is not None:
            comment.root = parent.root if parent.root is not None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        # 发送邮件通知
        comment.send_mail()

        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['comment_time'] = localtime(comment.comment_time).strftime("%Y-%m-%d %H:%M:%S")
        data['text'] = comment.text
        if parent is not None:
            data['reply_to'] = comment.reply_to.username
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if comment.root is not None else ''
    else:
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)
