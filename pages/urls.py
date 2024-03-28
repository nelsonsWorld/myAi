from django.urls import path
from . import views

#from .views import home_page_view

urlpatterns = [
    #path("", home_page_view, name="home"),
       # ex: /polls/
    path("", views.index, name="index"),
]