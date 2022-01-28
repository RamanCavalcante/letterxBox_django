from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Movie(models.Model):
    nome_movie = models.CharField(max_length=100)
    nome_diretor = models.CharField(max_length=100)
    genero_movie = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    img_movie = models.ImageField(upload_to='catalogo/static/cars')


      