from django.urls import path, re_path
from .views import ListSuperherosView, ListSuperherosByGenderView


urlpatterns = [
    path('superheros/', ListSuperherosView.as_view(), name="superheros-all"),
    re_path('^superheros/gender/(?P<gender>.+)/$', ListSuperherosByGenderView.as_view(), name="superheros-gender")
]