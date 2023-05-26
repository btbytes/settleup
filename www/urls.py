from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newtable", views.new_table, name="new_table"),
    path("table/<int:table_id>", views.table, name="table"),
    path("table/<int:table_id>/addplayer", views.add_player, name="add_player"),
    path(
        "table/<int:table_id>/<int:player_id>/addbuyin",
        views.add_buyin,
        name="add_buyin",
    ),
    path("table/<int:table_id>/qrcode", views.table_qrcode, name="qrcode"),
]
