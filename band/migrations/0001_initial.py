# Generated by Django 3.0.6 on 2020-05-07 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bandname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandname_text', models.CharField(max_length=255, verbose_name='Band Name')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
