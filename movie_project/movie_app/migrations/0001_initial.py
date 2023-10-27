# Generated by Django 4.2.5 on 2023-10-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
