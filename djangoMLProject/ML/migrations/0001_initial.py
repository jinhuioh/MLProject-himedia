# Generated by Django 3.2.13 on 2022-05-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week1', models.CharField(max_length=10)),
                ('week2', models.CharField(max_length=10)),
                ('hour', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('size', models.IntegerField()),
                ('tag_click', models.IntegerField()),
            ],
        ),
    ]
