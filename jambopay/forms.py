from django.forms import ModelForm
from .models import Customer, Business

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'date_of_birth', 'nationality']

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['owner', 'name', 'category', 'registration_date', 'location_information']
