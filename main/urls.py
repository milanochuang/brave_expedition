from django.urls import path

from . import views

urlpatterns = [
path("question", views.question, name="question"),
path("<int:id>",views.index, name = "index"),
path("home", views.home, name="home"),
path("correct",views.correct, name="correct"),
path("incorrect", views.incorrect, name="incorrect"),
path("stuff",views.stuff, name="stuff"),
path("hello_django", views.hello_django, name="hello_django"),
path("background/",views.background, name="background"),
path("maps/", views.maps, name="maps")

]