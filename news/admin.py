from django.contrib import admin
from news.models import Categories, Users, News

# Register your models here.
admin.site.register(Categories)
admin.site.register(Users)
admin.site.register(News)
