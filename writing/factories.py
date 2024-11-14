import factory.fuzzy
from library.test_data import books_data

from .models import Writing


class WritingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Writing

    title = factory.fuzzy.FuzzyChoice([book["title"] for book in books_data])
    author = factory.SubFactory("author.factories.AuthorFactory")
    genre = factory.SubFactory("genre.factories.GenreFactory")
    publication_year = factory.fuzzy.FuzzyInteger(1900, 2022)
