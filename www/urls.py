from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newtable", views.new_table, name="new_table"),
]
