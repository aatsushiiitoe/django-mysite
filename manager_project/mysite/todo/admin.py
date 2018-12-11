from django.contrib import admin

from .models import Post,Todo,Detail

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('message','link','created_date',)
    list_display_links = ('message','link','created_date',)
    list_filter = ['created_date']

    
class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_text', 'pub_date')
    
class DetailInline(admin.TabularInline):
    model = Detail
    extra = 3
                    
admin.site.register(Post,PostAdmin)
admin.site.register(Todo,TodoAdmin)
admin.site.register(Detail)

# Register your models here.
