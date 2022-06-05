# Generated by Django 4.0.5 on 2022-06-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, default='', max_length=100)),
                ('title', models.CharField(blank=True, default='', max_length=500)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]