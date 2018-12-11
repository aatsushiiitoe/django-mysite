from django.contrib import admin

from .models import Post

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    list_display = ('message','link','created_date',)
    list_display_links = ('message','link','created_date',)
    list_filter = ['created_date']
    
admin.site.register(Post,PostAdmin)
# Register your models here.
