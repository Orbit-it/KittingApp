# Generated by Django 4.2.11 on 2024-05-21 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bon_de_sortie_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.bon_de_sortie'),
        ),
    ]
