from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writing__title',
        'writing__publication_year',
        'writing__author',
        'status',
    )
    list_filter = ('writing__publication_year', 'writing__author')
    search_fields = (
        'title',
        'writing__author__first_name',
        'writing__author__last_name',
        'writing__publication_year',
    )
    filter_horizontal = ('translators',)

    def status(self, obj):
        if obj.borrowers.filter(return_date__isnull=True).exists():
            return 'Borrowed'
        else:
            return 'On shelf'
