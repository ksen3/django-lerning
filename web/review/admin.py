from django.contrib import admin
from .models import review

class reviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName']

admin.site.register(review, reviewAdmin)