# Generated by Django 4.2.1 on 2023-06-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_project_alter_dusting_options_alter_dusting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='yarn',
            name='projects',
            field=models.ManyToManyField(to='main_app.project'),
        ),
    ]
