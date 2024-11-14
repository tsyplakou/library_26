import factory.fuzzy

from library.test_data import authors_data
from author.models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.fuzzy.FuzzyChoice([
        author['first_name'] for author in authors_data
    ])
    last_name = factory.fuzzy.FuzzyChoice([
        author['last_name'] for author in authors_data
    ])
    birth_date = factory.Faker('date')
    death_date = factory.Faker('date')
    biography = factory.Faker('paragraph')
    # image_path = factory.django.ImageField(filename='author.jpg')
