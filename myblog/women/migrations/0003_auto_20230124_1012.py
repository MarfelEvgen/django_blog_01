# Generated by Django 3.2.16 on 2023-01-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_auto_20230124_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='women',
        ),
        migrations.AddField(
            model_name='women',
            name='tag',
            field=models.ManyToManyField(to='women.Tags'),
        ),
    ]
