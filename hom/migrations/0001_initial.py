# Generated by Django 4.0.2 on 2022-04-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.TextField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
