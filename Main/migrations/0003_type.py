# Generated by Django 3.2.7 on 2021-12-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]