from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'death_date', 'image_path')
    list_filter = ('birth_date', 'death_date')
    list_editable = ('death_date',)
    search_fields = ('first_name', 'last_name')
    fields = ('first_name', 'last_name', 'birth_date', 'death_date', 'biography', 'image_path')
    ordering = ('last_name', 'first_name')
