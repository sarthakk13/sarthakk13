from django.urls import path
from . import views

urlpatterns = {
    path("", views.index, name = "index"),
    path("Sarthak", views.Sarthak, name = "Sarthak"),
    path("<str:name>", views.greet, name = "greet")
}
