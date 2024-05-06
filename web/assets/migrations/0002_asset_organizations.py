# Generated by Django 4.2.3 on 2024-04-30 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_organization_name'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='organizations',
            field=models.ForeignKey(default='614c935f-2b80-4cd2-bf38-54b57d1a5c22', on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='organizations.organization'),
            preserve_default=False,
        ),
    ]