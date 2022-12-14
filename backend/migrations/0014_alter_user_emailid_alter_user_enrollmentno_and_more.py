# Generated by Django 4.1.2 on 2022-11-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='EmailId',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='EnrollmentNo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
