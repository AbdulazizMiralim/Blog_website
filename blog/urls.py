from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category_list, name="category"),
    path('article/<int:pk>/', article_detail, name='article'),
    path('categories/<int:id>/', category_detail, name='categories'),
    path('login/', user_login, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', user_logout, name='logout'),

]