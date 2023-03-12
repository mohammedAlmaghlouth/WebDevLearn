from django.urls import path
from . import views

urlpatterns = [
    # default url website/hello
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
