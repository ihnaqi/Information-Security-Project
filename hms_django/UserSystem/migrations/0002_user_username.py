# Generated by Django 3.2.16 on 2022-12-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='mbt', max_length=255),
            preserve_default=False,
        ),
    ]
