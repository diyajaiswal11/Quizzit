# Generated by Django 3.0.6 on 2020-06-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0012_auto_20200609_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.IntegerField(default=6),
        ),
    ]
