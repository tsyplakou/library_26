from django.shortcuts import redirect, render
from .models import Genre
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def get_genres_cached():
    genres = cache.get('genres')

    if not genres:
        genres = Genre.objects.all()
        cache.set('genres', genres, timeout=4)

    return genres


# @cache_page(timeout=7)  # 7 secs
def genres(request):
    print('not cached')
    if request.method == 'GET':
        genres = get_genres_cached()
        return render(request, 'genres.html', {'genres': genres})


def genre(request, genre_id):
    if request.method == 'GET':
        genre = Genre.objects.get(id=genre_id)
        return render(
            request,
            'genre.html',
            {'genre': genre},
        )


def add_genre(request):
    if request.method == 'POST':
        Genre.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        return redirect('genres')

    return render(request, 'add_genre.html')


def edit_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)

    if request.method == "POST":
        genre.name = request.POST['name']
        genre.description = request.POST['description']
        genre.save()
        return redirect('genre', genre_id=genre_id)

    return render(request, 'edit_genre.html', {'genre': genre})
