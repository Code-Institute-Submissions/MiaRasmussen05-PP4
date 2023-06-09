# Generated by Django 3.2.18 on 2023-04-29 03:56

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('live_link', models.URLField(blank=True, max_length=250, null=True)),
                ('git_link', models.URLField(blank=True, max_length=250, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
