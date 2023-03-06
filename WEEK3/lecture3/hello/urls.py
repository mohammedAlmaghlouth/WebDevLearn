from django.urls import path
from . import views

urlpatterns = [
    # default url website/hello
    path("", views.index, name="index"),
    path("mohammed", views.mohammed, name="mohammed"),
    path("<str:name>", views.greet, name="greet")
]