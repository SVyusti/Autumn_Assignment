# Generated by Django 4.1.2 on 2022-10-29 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_candidates_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='RId',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.round'),
        ),
    ]
