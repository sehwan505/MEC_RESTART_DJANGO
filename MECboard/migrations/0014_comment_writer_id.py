# Generated by Django 2.2.4 on 2020-03-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0013_auto_20200319_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='writer_id',
            field=models.IntegerField(null=True),
        ),
    ]
