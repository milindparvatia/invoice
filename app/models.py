from django.db import models

TYPE_CHOICES = [('goods', 'Goods'),
                ('services', 'Services')]

TAX_CHOICES = [('tax', 'taxable'),
               ('non', 'nontaxable')]

INFO_CHOICES = [('sales', 'sales'),
                ('purchase', 'purchase')]

CUST_CHOICES = [('v', 'Vendor'),
                ('c', 'Client')]

GEN_CHOICES = [('MR', 'Mr.'),
               ('MRS', 'Mrs.')]

CURR_CHOICES = [('inr', 'INR'),
                ('usd', 'USD')]

GST_CHOICES = [('A', 'A'),
               ('B', 'B')]

PAY_CHOICES = [('paytm', 'PAYTM'),
               ('cod', 'COD')]

COUN_CHOICES = [('India', 'INDIA'),
                ('USA', 'USA')]

CITY_CHOICES = [('A', 'A'),
                ('B', 'B')]


STATE_CHOICES = [('A', 'A'),
                 ('B', 'B')]


class Items(models.Model):
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    profile_pic = models.ImageField(
        upload_to='media_data')
    item_name = models.CharField(max_length=50)
    sku = models.PositiveIntegerField()
    unit = models.PositiveIntegerField()
    hsn_sac = models.CharField(max_length=50)
    tax = models.CharField(choices=TAX_CHOICES, max_length=10)
    information = models.CharField(choices=INFO_CHOICES, max_length=10)
    rate = models.FloatField()
    amount = models.FloatField()
    description = models.CharField(max_length=100, blank=True, default='')


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    customer = models.CharField(choices=CUST_CHOICES, max_length=20)
    gender = models.CharField(choices=GEN_CHOICES, max_length=20)
    mobile = models.PositiveIntegerField()
    work = models.PositiveIntegerField()
    email = models.EmailField()
    company = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    skype = models.CharField(max_length=150)
    dept = models.CharField(max_length=100)


class Other_details(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE)
    gst_treatment = models.CharField(choices=GST_CHOICES, max_length=20)
    tax = models.CharField(choices=TAX_CHOICES, max_length=10)
    currency = models.CharField(choices=CURR_CHOICES, max_length=20)
    gst_number = models.PositiveIntegerField()
    place = models.CharField(max_length=100)
    payment = models.CharField(choices=PAY_CHOICES, max_length=20)


class Address(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE)
    country = models.CharField(choices=COUN_CHOICES, max_length=120)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    city = models.CharField(choices=CITY_CHOICES, max_length=120)
    state = models.CharField(choices=STATE_CHOICES, max_length=120)
    pincode = models.PositiveIntegerField()


class Notes(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE)
    note = models.TextField(max_length=150, default='Type your Note here...')
