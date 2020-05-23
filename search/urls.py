from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # search
    re_path(r'^item-(?P<class_id>\d+)-(?P<tag_id>\d+)', views.multi_search),
]
