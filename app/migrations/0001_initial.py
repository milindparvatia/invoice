# Generated by Django 2.1.5 on 2019-02-14 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('India', 'INDIA'), ('USA', 'USA')], max_length=120)),
                ('add1', models.CharField(max_length=100)),
                ('add2', models.CharField(max_length=100)),
                ('city', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=120)),
                ('state', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=120)),
                ('pincode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('customer', models.CharField(choices=[('v', 'Vendor'), ('c', 'Client')], max_length=20)),
                ('gender', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.')], max_length=20)),
                ('mobile', models.PositiveIntegerField()),
                ('work', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=150)),
                ('skype', models.CharField(max_length=150)),
                ('dept', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('goods', 'Goods'), ('services', 'Services')], max_length=10)),
                ('profile_pic', models.ImageField(upload_to='media_data')),
                ('item_name', models.CharField(max_length=50)),
                ('sku', models.PositiveIntegerField()),
                ('unit', models.PositiveIntegerField()),
                ('hsn_sac', models.CharField(max_length=50)),
                ('tax', models.CharField(choices=[('tax', 'taxable'), ('non', 'nontaxable')], max_length=10)),
                ('information', models.CharField(choices=[('sales', 'sales'), ('purchase', 'purchase')], max_length=10)),
                ('rate', models.FloatField()),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='Type your Note here...', max_length=150)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Other_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_treatment', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=20)),
                ('tax', models.CharField(choices=[('tax', 'taxable'), ('non', 'nontaxable')], max_length=10)),
                ('currency', models.CharField(choices=[('inr', 'INR'), ('usd', 'USD')], max_length=20)),
                ('gst_number', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=100)),
                ('payment', models.CharField(choices=[('paytm', 'PAYTM'), ('cod', 'COD')], max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Customer'),
        ),
    ]
