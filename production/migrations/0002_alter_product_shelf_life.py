# Generated by Django 5.1.3 on 2024-12-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shelf_life',
            field=models.IntegerField(verbose_name='Срок годности в мес.'),
        ),
    ]