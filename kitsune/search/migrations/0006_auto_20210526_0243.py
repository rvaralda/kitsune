# Generated by Django 2.2.20 on 2021-05-26 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20200629_0826'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.DeleteModel(
            name='Synonym',
        ),
    ]
