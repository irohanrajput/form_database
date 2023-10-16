from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form_view, name="form"),
    path('index', views.index_view, name = "index")
]
