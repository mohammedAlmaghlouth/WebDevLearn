from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def today(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    return render(request, "newyear/today.html", {
        "year": year,
        "month": month,
        "day": day
    })


def isNewYear(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    return render(request, "newyear/isnewyear.html", {
        "isnewyear": (month == 1) and (day == 1)
    })


def index(request):
    return HttpResponse("Type path of required date")
