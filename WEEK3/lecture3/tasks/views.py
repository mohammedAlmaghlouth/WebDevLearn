from django.shortcuts import render

tasks = ["foo", "bar", "baz", "jojoj"]
# Create your views here.


def index(request):
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "tasks/add.html")
