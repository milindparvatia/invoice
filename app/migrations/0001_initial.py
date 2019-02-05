# Generated by Django 2.1.5 on 2019-02-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('goods', 'Goods'), ('services', 'Services')], max_length=10)),
                ('image', models.ImageField(upload_to='media_data')),
                ('item_name', models.TextField(max_length=50)),
                ('sku', models.PositiveIntegerField()),
                ('unit', models.PositiveIntegerField()),
                ('hsn_sac', models.TextField(max_length=50)),
                ('tax', models.CharField(choices=[('tax', 'taxable'), ('non', 'nontaxable')], max_length=10)),
                ('information', models.CharField(choices=[('sales', 'sales'), ('purchase', 'purchase')], max_length=10)),
                ('rate', models.FloatField()),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
