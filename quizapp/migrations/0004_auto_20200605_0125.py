# Generated by Django 3.0.6 on 2020-06-04 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_auto_20200605_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice3',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice4',
        ),
    ]