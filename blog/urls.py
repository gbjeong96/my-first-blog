from django.urls import path #django함수인 path를 가져온다.
from . import views #blog app에서 사용할 모든 views를 가져온다.

urlpatterns = [
    path('', views.post_list, name= 'post_list'), #views.post_list라는 view를 post_list라는 이름을 가지도록 설정했다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #post/pk/에 pk라는 변수로 view에 전달을 한다. views.post_detail라는 view를 post_detail이라 이름을 붙이도록 설정했다.
]

