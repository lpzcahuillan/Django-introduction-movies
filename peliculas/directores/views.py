from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Director, Pelicula

class DirectorListView(ListView):
    model = Director

class DirectorDetailView(DetailView):
    model = Director

class PeliculaListView(ListView):
    model = Pelicula

class PeliculaDetailView(DetailView):
    model = Pelicula

