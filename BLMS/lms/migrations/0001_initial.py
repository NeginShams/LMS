# Generated by Django 3.0.4 on 2020-11-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('userID', models.PositiveIntegerField(max_length=15, primary_key=True, serialize=False)),
                ('content', models.TextField(default='')),
                ('date_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
