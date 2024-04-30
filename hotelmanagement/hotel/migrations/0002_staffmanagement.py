# Generated by Django 5.0 on 2024-03-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffmanagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('workingas', models.CharField(max_length=255)),
                ('intimehr', models.IntegerField()),
                ('intimemin', models.IntegerField()),
                ('outtimehr', models.IntegerField()),
                ('outtimemin', models.IntegerField()),
                ('shiftno', models.IntegerField()),
                ('paycheck', models.IntegerField()),
            ],
        ),
    ]
