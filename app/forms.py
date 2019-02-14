from .models import Items
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
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
