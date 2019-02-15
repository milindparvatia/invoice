from .models import Items, Customer, Address, Other_details, Notes
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
        self.helper.add_input(Submit('submit', 'Submit'))


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
