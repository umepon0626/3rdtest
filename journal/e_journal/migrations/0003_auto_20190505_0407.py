# Generated by Django 2.1.1 on 2019-05-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_journal', '0002_e_journal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_journal',
            name='photo',
            field=models.ImageField(default='documents', upload_to='documents/'),
        ),
    ]
