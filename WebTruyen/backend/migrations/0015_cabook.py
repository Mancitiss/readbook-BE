# Generated by Django 3.2.16 on 2023-10-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_chapter_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_id', models.IntegerField(default=0)),
                ('category_id', models.IntegerField(default=0)),
            ],
        ),
    ]
