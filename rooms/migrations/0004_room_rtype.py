# Generated by Django 2.2 on 2019-05-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20190410_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rtype',
            field=models.CharField(default='room', max_length=10),
        ),
    ]
