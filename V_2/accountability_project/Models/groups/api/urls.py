from django.urls import path
from Models.groups.api.api import group_api_view, group_datail_api_view, post_api_view, post_datail_api_view

urlpatterns = [
    path('group/', group_api_view, name = 'group_api'),
    path('group/<int:pk>', group_datail_api_view, name = 'group_datail_api_view'),
    path('post/', post_api_view, name = 'post_api_view'),
    path('post/<int:pk>', post_datail_api_view, name = 'post_datail_api_view')
]