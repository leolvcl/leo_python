# Generated by Django 2.0.2 on 2018-04-04 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_article_create_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='create_time',
            new_name='create_date',
        ),
    ]