from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^item-(?P<class_id>\d+)-(?P<tag_id>\d+)', views.multi_search),
]
