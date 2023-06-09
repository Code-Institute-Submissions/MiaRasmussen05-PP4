# Generated by Django 3.2.18 on 2023-04-30 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_gallerycategory_images'),
        ('user_profile', '0004_auto_20230430_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.shop')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='user_profile.order')),
            ],
        ),
    ]
