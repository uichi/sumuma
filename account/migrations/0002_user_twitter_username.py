# Generated by Django 4.0.5 on 2022-09-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter_username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='twitter_username'),
        ),
    ]
