# Generated by Django 2.0.7 on 2019-03-28 09:43

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('decisiontree', '0002_remove_product_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('decision_tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decisiontree.DecisionTree')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
