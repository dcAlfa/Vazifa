# Generated by Django 4.0.4 on 2022-04-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_project_sana'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_raqam',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='kurs',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
