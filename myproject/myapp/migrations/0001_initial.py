# Generated by Django 2.0.1 on 2018-01-31 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=500, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('passw', models.CharField(max_length=100)),
            ],
        ),
    ]
