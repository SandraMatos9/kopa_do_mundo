# from django.contrib import admin
from django.urls import path
from .views import TeamView,TeamDetails
#precisa manter o nome urlpatterns
urlpatterns = [
    path("teams/",TeamView.as_view()),
    path("teams/<int:team_id>/",TeamDetails.as_view())
]