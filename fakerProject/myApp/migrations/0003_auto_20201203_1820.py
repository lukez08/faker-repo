# Generated by Django 2.2.2 on 2020-12-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_student_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marks',
            field=models.IntegerField(),
        ),
    ]
