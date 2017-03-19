from django.contrib import admin
from .models import Article

# Register your models here.

admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

admin.site.register(Article,ArticleAdmin)
