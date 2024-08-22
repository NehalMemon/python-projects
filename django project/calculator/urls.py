from django.urls import path
from . import views


urlpatterns = [
    path("", views.add, name='sum'),
    path("", views.avg, name='average'),
    path("", views.product, name='production'),
]