from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return (
            f'{self.first_name} {self.last_name} '
            f'({self.birth_date.year} - '
            f'{self.death_date.year if self.death_date else "present"  })'
        )
