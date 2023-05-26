from django.shortcuts import render
from datetime import datetime
from django.urls import reverse


def index(request):
    context = {"date": datetime.today()}
    return render(request, "www/index.html", context)


def new_table(request):
    return render(request, "www/new_table.html")


def table(request, table_id):
    context = {"table_id": table_id}
    return render(request, "www/table.html", context)


def add_player(request, table_id):
    context = {"table_id": table_id}
    return render(request, "www/add_player.html", context)


def add_buyin(request, table_id, player_id):
    context = {"table_id": table_id, "player_id": player_id}
    return render(request, "www/add_buyin.html", context)


def table_qrcode(request, table_id):
    context = {"table_id": table_id}
    url = "https://www.settleup.com" + reverse("table", args=[table_id])
    context["url"] = url
    return render(request, "www/qrcode.html", context)
