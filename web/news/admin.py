from django.contrib import admin

# Register your models here.
from .models import article

class articleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'anons', 'date']
    list_display_links = ['id', 'title']


admin.site.register(article, articleAdmin)
