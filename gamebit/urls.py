from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingPageView.as_view(),name="home"),
    path("store",views.storePageView.as_view(),name="store"),
    path("game/<slug:slug>", views.Gamedetails.as_view(), name="game-detail"),
    path("library", views.Library.as_view(), name="library")
]

