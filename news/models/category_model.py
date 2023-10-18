from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
