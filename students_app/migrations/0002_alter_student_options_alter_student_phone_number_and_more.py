# Generated by Django 4.0.6 on 2022-07-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('first_name', 'last_name', 'date_of_birth')},
        ),
    ]
