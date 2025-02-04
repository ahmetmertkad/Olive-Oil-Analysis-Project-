# Generated by Django 5.0.6 on 2024-06-05 14:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OliveOil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('oil_type', models.CharField(choices=[('EVOO', 'Extra Virgin Olive Oil (EVOO)'), ('VOO', 'Virgin Olive Oil (VOO)'), ('ROO', 'Refined Olive Oil (ROO)'), ('OO', 'Olive Oil (OO)')], max_length=4)),
                ('acidity', models.FloatField()),
                ('peroxide_value', models.FloatField()),
                ('k232', models.FloatField()),
                ('k270', models.FloatField()),
                ('delta_k', models.FloatField()),
                ('total_polyphenols', models.FloatField()),
                ('moisture_and_volatiles', models.FloatField()),
                ('pyropheophytins', models.FloatField()),
                ('dag_content', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olive_oils', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
