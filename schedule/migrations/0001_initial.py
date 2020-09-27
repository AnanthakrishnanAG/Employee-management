# Generated by Django 3.1.1 on 2020-09-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'ActivityPeriod',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=20)),
                ('real_name', models.CharField(max_length=50)),
                ('tz', models.CharField(max_length=50)),
                ('activity_periods', models.ManyToManyField(null=True, related_name='activity_periods', to='schedule.ActivityPeriod')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
