import factory
from .models import Genre
from library.test_data import genres_data


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre
        django_get_or_create = ('name',)

    name = factory.fuzzy.FuzzyChoice(genre['name'] for genre in genres_data)
    description = factory.fuzzy.FuzzyChoice(genre['description'] for genre in genres_data)
