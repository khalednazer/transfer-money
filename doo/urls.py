from django.urls import path 
from . import views

urlpatterns = [
    path('form/', views.form, name='forms'),
    path('seucces/', views.succ, name='seucces'),
    path('create/', views.create, name='create'),
    path('', views.tem, name='main'),
    path('trans', views.trans, name='trans'),
    path('data', views.data, name='data'),
    path('myaccount', views.account, name='MYacc'),
    path('acc/<int:pk>', views.Acc, name='acc'),
]


# https://github.com/divanov11/buydenniscoffees_startingfiles/blob/master/base/templates/base/success.html
#https://www.youtube.com/watch?v=oZwyA9lUwRk&list=PL-51WBLyFTg38qZ0KHkJj-paDQAAu9HiP&ab_channel=DennisIvy
# https://chatgpt.com/c/6744e76d-4868-8003-81a5-193a63f9aef7