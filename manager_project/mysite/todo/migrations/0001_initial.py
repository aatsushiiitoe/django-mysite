# Generated by Django 2.0.6 on 2018-11-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100, verbose_name='タスク')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
        ),
    ]
