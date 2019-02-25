from .models import Items, Customer, Address, Other_details, Notes, Bill, PurchaseOrder
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = [
            'type',
            'profile_pic',
            'item_name',
            'sku',
            'unit',
            'hsn_sac',
            'tax',
            'information',
            'rate',
            'amount',
            'description'
        ]

    def __init__(self, *args, **kwargs):
        super(ItemsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.add_input(Submit('submit', 'Submit'))


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'customer',
            'gender',
            'mobile',
            'work',
            'email',
            'company',
            'website',
            'skype',
            'dept'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['first_name'].widget.attrs = {'placeholder': 'First name'}
        self.fields['last_name'].widget.attrs = {'placeholder': 'Last name'}
        self.fields['customer'].widget.attrs = {'placeholder': 'Type of Customer'}
        self.fields['mobile'].widget.attrs = {'placeholder': 'Contact No.(mobile)'}
        self.fields['work'].widget.attrs = {'placeholder': 'Contact No.(work)'}
        self.fields['email'].widget.attrs = {'placeholder': 'Email'}
        self.fields['company'].widget.attrs = {'placeholder': 'Company Name'}
        self.fields['website'].widget.attrs = {'placeholder': 'Website'} 
        self.fields['dept'].widget.attrs = {'placeholder': 'Designation Department'}
        self.fields['skype'].widget.attrs = {'placeholder': 'Skype Name'}

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'country',
            'add1',
            'add2',
            'city',
            'state',
            'pincode'
        ]

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class OtherDetailsForm(forms.ModelForm):
    class Meta:
        model = Other_details
        fields = [
            'gst_treatment',
            'tax',
            'currency',
            'gst_number',
            'place',
            'payment'
        ]

    def __init__(self, *args, **kwargs):
        super(OtherDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [
            'note'
        ]

    def __init__(self, *args, **kwargs):
        super(NotesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            'vendor_name',
            'bills',
            'order_number',
            'bill_date',
            'due_date',
            'payment_terms'
        ]

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['vendor_name'].widget.attrs = {'placeholder': 'Vendor name'}
        self.fields['bills'].widget.attrs = {'placeholder': 'Bills'}
        self.fields['order_number'].widget.attrs = {'placeholder': 'order number'}
        self.fields['bill_date'].widget.attrs = {'placeholder': 'Bill Date'}
        self.fields['due_date'].widget.attrs = {'placeholder': 'Due Date'}
        self.fields['payment_terms'].widget.attrs = {'placeholder': 'Payment Terms'}

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = [
            'vendor_name',
            'purchase_order_number',
            'reference_number',
            'date',
            'delivery_date',
            'shipment_preference'
        ]

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['vendor_name'].widget.attrs = {'placeholder': 'Vendor name'}
        self.fields['purchase_order_number'].widget.attrs = {'placeholder': 'purchase order number'}
        self.fields['reference_number'].widget.attrs = {'placeholder': 'reference number'}
        self.fields['date'].widget.attrs = {'placeholder': 'Date'}
        self.fields['delivery_date'].widget.attrs = {'placeholder': 'delivery date'}
        self.fields['shipment_preference'].widget.attrs = {'placeholder': 'shipment preference'}
