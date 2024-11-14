import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=80)

    translators = models.ManyToManyField(
        'author.Author',
        related_name='translated_books',
        help_text='Translators of the book.',
    )
    borrowers = models.ManyToManyField(
        'user.User',
        limit_choices_to={'role': 'reader'},
        related_name='borrowed_books',
        help_text='Users who have borrowed the book.',
        blank=True,
        through='book.Borrowing',
    )


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    reader = models.ForeignKey(
        'user.User',
        limit_choices_to={'role': 'reader'},
        related_name='borrowings',
        on_delete=models.PROTECT,
    )
    book = models.ForeignKey(
        'book.Book',
        related_name='borrowings',
        on_delete=models.PROTECT,
    )

    @property
    def status(self):
        if self.return_date:
            return 'Returned'
        elif self.due_date < datetime.date.today():
            return 'Overdue'
        else:
            return 'Borrowed'

    def __str__(self):
        return f"{self.reader} - {self.book} ({self.status})"
