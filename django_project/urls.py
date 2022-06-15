from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', greeting),
    path('about/', view_about),
    path('get/data', manual_form, name="manual_form"),
    path('get/data-django-form/', django_form, name="django_form"),

    path('scoreboard/', include('scoreboard.urls')),
]
