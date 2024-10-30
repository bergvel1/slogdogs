from django.urls import path
from . import views

app_name = "members"
urlpatterns = [
    path('', views.members, name='members'),
    path('details/<slug:slug>', views.details, name='details'),
]