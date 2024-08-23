from django.urls import path
from . import views


urlpatterns = [
    path("total/", views.add, name='total'),
    path("avg/", views.avg, name='average'),
    path("pro/", views.product, name='production'),
]