# Generated by Django 5.0.1 on 2024-03-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='themes_list')),
                ('mavzular', models.CharField(max_length=15000, verbose_name='themes_list')),
            ],
            options={
                'verbose_name': 'themes_list',
                'db_table': 'mavzular',
            },
        ),
    ]
