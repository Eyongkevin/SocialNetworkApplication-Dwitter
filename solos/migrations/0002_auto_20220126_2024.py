# Generated by Django 3.2.5 on 2022-01-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='artist',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='instrument',
            field=models.CharField(default='n/a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='track',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
    ]
