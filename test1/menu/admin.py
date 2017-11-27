from django.contrib import admin
from .models import Food
# Register your models here.
class Food_admin(admin.ModelAdmin):
    list_display = ['title','parent']
    list_filter = ['title','parent']
    search_fields = ['title','parent']



admin.site.register(Food,Food_admin)