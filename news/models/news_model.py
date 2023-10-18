from django.db import models
from django.forms import ValidationError
from news.models.user_model import Users
from news.models.category_model import Categories
from datetime import datetime


def validate_title(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_date_format(value):
    if not datetime.strptime(str(value), "%Y-%m-%d"):
        raise ValidationError("A data deve estar no formato AAAA-MM-DD.")


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title])
    content = models.TextField()
    author = models.ForeignKey(
        Users, max_length=200, on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(validators=[validate_date_format])
    image = models.ImageField(null=True, blank=True, upload_to="img/")
    categories = models.ManyToManyField(Categories, related_name="news")

    def __str__(self) -> str:
        return self.title
