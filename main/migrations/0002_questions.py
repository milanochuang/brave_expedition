# Generated by Django 4.1.4 on 2023-01-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.CharField(max_length=200)),
                ('clicked', models.BooleanField()),
            ],
        ),
    ]
