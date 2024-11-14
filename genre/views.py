from django.shortcuts import redirect, render
from .models import Genre


def genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
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
