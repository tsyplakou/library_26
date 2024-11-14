from django.db import models


class Writing(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(
        'authors.Author',
        on_delete=models.PROTECT,
        related_name='books',
        help_text='Author of the book.',
    )
    genre = models.ForeignKey(
        'genres.Genre',
        on_delete=models.PROTECT,
        related_name='books',
        help_text='Genre of the book.',
    )
    publication_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} ({self.publication_year}) by {self.author}'
