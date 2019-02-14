from django.db import models

TYPE_CHOICES = [('goods', 'Goods'),
                ('services', 'Services')]

TAX_CHOICES = [('tax', 'taxable'),
               ('non', 'nontaxable')]

INFO_CHOICES = [('sales', 'sales'),
                ('purchase', 'purchase')]


class Items(models.Model):
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    # image = models.ImageField(upload_to='media_data')
    item_name = models.CharField(max_length=50)
    sku = models.PositiveIntegerField()
    unit = models.PositiveIntegerField()
    hsn_sac = models.CharField(max_length=50)
    tax = models.CharField(choices=TAX_CHOICES, max_length=10)
    information = models.CharField(choices=INFO_CHOICES, max_length=10)
    rate = models.FloatField()
    amount = models.FloatField()
    description = models.CharField(max_length=100, blank=True, default='')

# new model1111
