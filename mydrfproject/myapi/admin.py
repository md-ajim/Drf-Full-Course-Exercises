from django.contrib import admin
from myapi.models import * 


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author', 'published_date')
    search_fields =('title' , 'author')
    list_filter = ('langush' , 'published_date')

