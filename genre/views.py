from django.shortcuts import render
from .models import Genre


def genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        return render(request, 'genres.html', {'genres': genres})


def genre(request, genre_id):
    if request.method == 'GET':
        genre = Genre.objects.get(id=genre_id)
        return render(request, 'genre.html', {'genre': genre})
