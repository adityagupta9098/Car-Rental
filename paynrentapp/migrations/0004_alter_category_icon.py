# Generated by Django 3.2.5 on 2023-03-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0003_remove_category_iconee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
