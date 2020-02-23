from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views

from pokemon import views

urlpatterns = [
    path('trainers/', views.TrainerList.as_view()),
    path('trainers/<int:pk>/', views.TrainerDetail.as_view()),
    path('pokemons/', views.PartnerList.as_view()),
    path('pokemons/<int:pk>/', views.PartnerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)  # これ要る?

urlpatterns += [
    path('api-token-auth/', auth_views.obtain_auth_token)
]
