from django.urls import path
from . import views

urlpatterns = [
    # default url website/hello
    path("<str:name>", views.index, name="index"),

]
