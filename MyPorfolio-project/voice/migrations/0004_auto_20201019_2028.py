# Generated by Django 3.1 on 2020-10-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0003_voice_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice',
            name='level',
            field=models.CharField(default='', max_length=25),
        ),
    ]