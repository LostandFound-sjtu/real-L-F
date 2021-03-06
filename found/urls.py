from django.urls import path
from . import views

urlpatterns = [

    path('found/', views.found, name='found'),


    path('item/<int:id>/', views.found_item_details, name='found_item_details'),


    path('create_found_item/', views.create_found_item, name='create_found_item'),

    path('item/<int:id>/update/', views.found_item_update, name='found_item_update'),

    path('item/<int:id>/delete', views.found_item_delete, name='found_item_delete'),
    path('found_item/<int:id>/send_mail', views.found_item_send_mail, name='found_item_mail'),
    path('found/make/<kind_name_slug>/', views.make, name="make"),

]
