from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ajax_classify/<handle>/', views.ajax_classify, name='ajax_classify'),
    path('ajax_classify_tweet/', views.ajax_classify_tweet, name='ajax_classify_tweet'),
]
