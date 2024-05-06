# Generated by Django 4.2.3 on 2024-04-30 09:30

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'opencve_assets',
            },
        ),
    ]