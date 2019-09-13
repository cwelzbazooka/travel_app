from django.urls import path

from . import views

urlpatterns = [

    path('home/', views.Map_Travel.as_view(), name='map'),
    path('localisation/<int:localisation_id>/', views.localisation, name="localisation"),
    path('localisations/', views.localisations, name="localisations"),
    path('add_localisation/', views.add_localisation, name="add_localisation"),
]

