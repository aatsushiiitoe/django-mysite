from django.contrib import admin

from .models import Photo

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    list_display = ('image',)
       
