# Generated by Django 5.0.2 on 2024-02-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=64)),
                ('book_author', models.CharField(max_length=64)),
                ('tool_img', models.ImageField(upload_to='book_images')),
            ],
        ),
    ]
