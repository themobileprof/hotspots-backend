from django.urls import path

from . import views

urlpatterns = [
    path('collect/', views.collect_tweets, name='collect'),
    path('process/', views.process_tweets, name='process'),
]