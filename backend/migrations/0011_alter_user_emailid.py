# Generated by Django 4.1.2 on 2022-11-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_candidates_studentid_alter_question_questionid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='EmailId',
            field=models.EmailField(max_length=254),
        ),
    ]
