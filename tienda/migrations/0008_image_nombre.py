# Generated by Django 2.2.3 on 2019-10-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_auto_20191003_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='nombre',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
