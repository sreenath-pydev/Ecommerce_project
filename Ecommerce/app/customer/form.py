from django import forms
from .models import customers

class AddressForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['address', 'city', 'locality', 'phone','pincode']