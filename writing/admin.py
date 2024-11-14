from django.contrib import admin

from .models import Writing


@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'author', 'genre')
    list_filter = ('publication_year', 'author', 'genre')
    search_fields = ('title', 'author__first_name', 'author__last_name')
