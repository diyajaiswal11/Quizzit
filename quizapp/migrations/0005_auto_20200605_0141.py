# Generated by Django 3.0.6 on 2020-06-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20200605_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='enteredans',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(default='', max_length=100),
        ),
    ]
