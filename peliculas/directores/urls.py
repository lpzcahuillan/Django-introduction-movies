from django.urls import path
from .views import DirectorListView, DirectorDetailView, PeliculaListView, PeliculaDetailView

urlpatterns = [
    path('directores/', DirectorListView.as_view(), name='directores_list'),
    path('directores/<int:pk>/', DirectorDetailView.as_view(), name='director_detail'),
    path('peliculas/', PeliculaListView.as_view(), name='peliculas_list'),
    path('peliculas/<int:pk>/', PeliculaDetailView.as_view(), name='pelicula_detail'),
]
