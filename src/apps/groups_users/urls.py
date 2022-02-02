from django.urls import re_path
from src.apps.groups_users import views


app_name = 'groups_users'

urlpatterns = [
    re_path(r'^group_users/$', views.group_users_list),
    re_path(r'^group_users/(?P<pk>[0-9]+)$', views.group_users_detail),
]