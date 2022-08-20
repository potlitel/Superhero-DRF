from django.urls import path
from .views import ListSongsView


urlpatterns = [
    path('superheros/', ListSongsView.as_view(), name="superheros-all")
]