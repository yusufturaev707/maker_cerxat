# Generated by Django 4.0.1 on 2022-01-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='qr_code',
            field=models.ImageField(blank=True, default='qe.png', null=True, upload_to='qr_codes/'),
        ),
    ]