# Generated by Django 2.2.3 on 2019-10-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_remove_image_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('corrreo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Integrante',
                'verbose_name_plural': 'Integrantes',
            },
        ),
    ]
