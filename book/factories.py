import factory.fuzzy
from library.test_data import books_data

from .models import Book, Borrowing


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.fuzzy.FuzzyChoice([book["title"] for book in books_data])
    writing = factory.SubFactory("writing.factories.WritingFactory")

    @factory.post_generation
    def borrowers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for borrower in extracted:
                self.borrowers.add(borrower)


class BorrowingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Borrowing

    book = factory.SubFactory(BookFactory)
    borrow_date = factory.Faker("date")
    due_date = factory.Faker("date")
    return_date = factory.Faker("date")
    reader = factory.SubFactory("user.factories.ReaderFactory")
