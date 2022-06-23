from django.urls import path

from scoreboard.views import *

app_name = 'scoreboard'

urlpatterns = [
    path('get/data-django-form-model/', django_form_model, name="django_form_model"),
    path('list/team/', list_team, name="list_team"),
    path('change/team/<str:name>/', change_team, name="change_team"),
    path('remove/team/<str:name>', remove_team, name="remove_team"),

    path('create/soccerplayer/', create_soccerplayer, name="create_soccerplayer"),
    path('list/soccerplayer/', list_soccerplayer, name="list_soccerplayer"),
    path('change/soccerplayer/<int:id>/', change_soccerplayer, name="change_soccerplayer"),
    path('remove/soccerplayer/<int:idsp>', remove_soccerplayer, name="remove_soccerplayer"),


    
]
