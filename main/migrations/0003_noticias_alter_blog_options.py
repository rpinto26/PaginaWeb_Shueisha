# Generated by Django 4.1.1 on 2022-09-21 08:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reviews_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog Profiles',
                'ordering': ['timestamp'],
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['timestamp'], 'verbose_name': 'Obra', 'verbose_name_plural': 'Obras'},
        ),
    ]
