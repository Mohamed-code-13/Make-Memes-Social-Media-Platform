from django.contrib import admin

# Register your models here.
from MakeMemes.models import Post, Search

admin.site.register(Post)
admin.site.register(Search)
