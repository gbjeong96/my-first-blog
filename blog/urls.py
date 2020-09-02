from django.urls import path #django함수인 path를 가져온다.
from . import views #blog app에서 사용할 모든 views를 가져온다.

urlpatterns = [
    path('', views.post_list, name= 'post_list'),
]
