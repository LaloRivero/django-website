# Generated by Django 3.1 on 2020-09-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200905_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='image',
            field=models.URLField(default=''),
        ),
    ]