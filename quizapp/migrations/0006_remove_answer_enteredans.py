# Generated by Django 3.0.6 on 2020-06-04 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_auto_20200605_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='enteredans',
        ),
    ]
