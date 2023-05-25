from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {"date": datetime.today()}
    return render(request, "www/index.html", context)
