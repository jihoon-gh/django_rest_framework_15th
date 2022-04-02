# Generated by Django 4.0.3 on 2022-03-31 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(to='api.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(to='api.profile'),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
