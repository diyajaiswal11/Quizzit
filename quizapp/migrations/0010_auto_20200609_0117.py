# Generated by Django 3.0.6 on 2020-06-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0009_auto_20200609_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(default=1, max_length=500),
        ),
        migrations.AlterField(
            model_name='level',
            name='score',
            field=models.CharField(default=0, max_length=2500),
        ),
    ]