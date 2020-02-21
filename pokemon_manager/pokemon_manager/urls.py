from django.urls import path
from pokemon import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('trainers/', views.TrainerList.as_view()),
    path('trainer/<int:pk>/', views.TrainerDetail.as_view()),
    path('pokemons/', views.PokemonList.as_view()),
    path('pokemon/<int:pk>/', views.PokemonDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns) # これ要る?