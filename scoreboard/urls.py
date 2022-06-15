from django.urls import path

from scoreboard.views import *

app_name = 'scoreboard'

urlpatterns = [
    path('get/data-django-form-model/', django_form_model, name="django_form_model"),
    path('list/team/', list_team, name="list_team"),
    path('change/team/<str:name>', change_team, name="change_team"),
    path('remove/team/<str:name>', remove_team, name="remove_team"),
]
