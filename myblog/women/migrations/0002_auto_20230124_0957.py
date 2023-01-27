# Generated by Django 3.2.16 on 2023-01-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create'], 'verbose_name': 'Famous women'},
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/women'),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('women', models.ManyToManyField(to='women.Women')),
            ],
        ),
    ]