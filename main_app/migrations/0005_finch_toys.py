# Generated by Django 3.0.8 on 2020-09-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200918_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]
