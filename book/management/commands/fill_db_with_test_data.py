from author.factories import AuthorFactory, Author
from book.factories import BookFactory
from django.core.management.base import BaseCommand
from library.test_data import (
    genres_data,
    authors_data,
    books_data,
)
from writing.factories import WritingFactory

from genre.factories import GenreFactory, Genre


class Command(BaseCommand):
    help = 'Fill db with data from test_data.'

    def handle(self, *args, **options):
        for genre_data in genres_data:
            GenreFactory(
                name=genre_data['name'],
                description=genre_data['description'],
            )

        for author_data in authors_data:
            author = AuthorFactory(
                first_name=author_data['first_name'],
                last_name=author_data['last_name'],
                birth_date='{}-01-01'.format(author_data['birth_year']),
                death_date=(
                    '{}-01-01'.format(author_data['death_year'])
                    if author_data['death_year'] else None
                ),
                biography='',
            )

        for book_data in books_data:
            last_name = book_data['author'].split()[-1]
            author = (
                Author.objects.filter(last_name=last_name).first() or
                Author.objects.first()
            )
            genre = Genre.objects.get_or_create(name=book_data['genre'])[0]
            writing = WritingFactory(
                title=book_data['title'],
                author=author,
                genre=genre,
                publication_year=book_data['release_date'].split('-')[0],
            )
            BookFactory(
                title=book_data['title'],
                writing=writing,
            )
