# Generated by Django 2.2.6 on 2021-01-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('body_weight', models.IntegerField()),
                ('title', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
            ],
        ),
    ]