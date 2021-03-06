# Generated by Django 3.1.4 on 2020-12-04 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('0', 'Female'), ('1', 'Male'), ('2', 'Other')], max_length=2)),
            ],
        ),
    ]
