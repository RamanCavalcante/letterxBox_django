from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):

    list_movies = Movie.objects.all()

    dados = {
      'list_movies' : list_movies
    }
    return render(request, 'index.html', dados)