from django.urls import path
from . import views

urlpatterns = [
    # default url website/hello
    path("today", views.today, name="today"),
    path("isnewyear", views.isNewYear, name="isnewyear"),
    path("", views.index, name="index")
]
