# Generated by Django 2.0.5 on 2018-06-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='perDayData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('DailyVar', models.IntegerField()),
            ],
        ),
    ]