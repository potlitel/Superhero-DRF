from django.urls import path
from .views import ListSuperherosView


urlpatterns = [
    path('superheros/', ListSuperherosView.as_view(), name="superheros-all")
]