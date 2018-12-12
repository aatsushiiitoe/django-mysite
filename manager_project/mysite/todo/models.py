import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    message = models.CharField(
        max_length=100,
        verbose_name="タスク",
    )
    link = models.CharField(
        max_length=100,
        verbose_name="リンク",
    )
    
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="登録日時",
        )


class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Detail(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    detail_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.detail_text

    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
