from django.urls import path
from . import views

urlpatterns = [
    path('lost/', views.lost, name="lost"),
    path('lost_item/<int:id>/', views.lost_item_details, name='lost_item_details'),
    path('create_lost_item/', views.create_lost_item, name='create_lost_item'),
    path('lost_item/<int:id>/update/', views.lost_item_update, name='lost_item_update'),

    path('lost_item/<int:id>/delete', views.lost_item_delete, name='lost_item_delete'),
    path('lost_item/<int:id>/send_mail', views.lost_item_send_mail, name='lost_item_mail'),
    path('data_fresh/', views.data_refresh, name = "data_fresh"),
    path('lost/make/<kind_name_slug>/', views.make, name="make"),
]
