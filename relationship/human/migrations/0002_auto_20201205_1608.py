# Generated by Django 3.1.4 on 2020-12-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=2),
        ),
    ]
