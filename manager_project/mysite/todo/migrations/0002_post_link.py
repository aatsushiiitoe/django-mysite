# Generated by Django 2.0.6 on 2018-11-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='please add link', max_length=100, verbose_name='リンク'),
            preserve_default=False,
        ),
    ]