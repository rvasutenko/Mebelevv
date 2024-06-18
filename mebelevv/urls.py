from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting_page"),
    path("gallery", views.GalleryPageView.as_view(), name="gallery_page")
]