# Generated by Django 5.0.2 on 2024-05-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checksheetresult',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
