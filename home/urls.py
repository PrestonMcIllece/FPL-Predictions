from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('input-team/', views.get_name, name="get-name"),
    path('values/', views.values, name='values'),
    path('input-team/team-suggestions/', views.suggest_players, name='suggest-players'),
    path('build-team/', views.build_team, name='from-scratch'),
    path('compare-players/', views.compare_players, name='compare-players'),
    path('compare-players/suggestions/', views.compare_players_suggestions, name='compare-players-suggestions')
]