from django.contrib import admin

from .models import Post,Todo,Detail,Choice, Question

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
class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
