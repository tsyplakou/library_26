import factory
from .models import Genre
from library.test_data import genres_data


class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.fuzzy.FuzzyChoice(genre['name'] for genre in genres_data)
    description = factory.fuzzy.FuzzyChoice(genre['description'] for genre in genres_data)
