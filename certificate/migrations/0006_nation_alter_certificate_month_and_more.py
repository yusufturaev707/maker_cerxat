# Generated by Django 4.0.1 on 2022-05-23 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0005_alter_certificate_sharf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('key', models.CharField(default='uz', max_length=3)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Millat',
                'verbose_name_plural': 'Millatlar',
            },
        ),
        migrations.AlterField(
            model_name='certificate',
            name='month',
            field=models.CharField(choices=[('yanvar', 'Yanvar'), ('fevral', 'Fevral'), ('mart', 'Mart'), ('aprel', 'Aprel'), ('may', 'May'), ('iyun', 'Iyun'), ('iyul', 'Iyul'), ('avgust', 'Avgust'), ('sentabr', 'Sentabr'), ('oktabr', 'Oktabr'), ('dekabr', 'Dekabr')], default='yanvar', max_length=50, verbose_name='Oy'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificate.nation'),
        ),
    ]
