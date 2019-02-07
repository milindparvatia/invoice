from .models import Items
from django import forms


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            'type',
            # 'image',
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
