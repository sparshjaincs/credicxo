# Generated by Django 2.2.6 on 2020-07-01 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='headquarter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='headquartes', to='bankapp.City', to_field='city_name'),
        ),
    ]