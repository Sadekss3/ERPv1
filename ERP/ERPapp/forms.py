from dataclasses import fields
from datetime import datetime
from email.policy import default
from itertools import product
from django.forms import ModelForm
from django import forms
from django.utils import timezone

from .models import Invoice_type, Payment_Method, Product, Client, Project, Invoice


class Product_Form(ModelForm):  # Note that it is not inheriting from forms.ModelForm
    class Meta:
        model = Product
        fields = ['name', 'unit', 'quantity', 'price', 'category']

class Client_Form(ModelForm):
    class Meta:
        model = Client
        fields = ['company_name', 'name', 'lastname', 'street', 'house_number', 'postal_code', 'town', 'phone_numer_1'
            , 'phone_number_2', 'TIN', 'email']

class DateInput(forms.DateInput):
    input_type = 'date'

class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client', 'start_time', 'scheduled_end_time', 'end_time', 'description',
                  'street', 'house_number', 'postal_code', 'town', 'budget']
        widgets = {
            'start_time': DateInput(),
            'scheduled_end_time': DateInput(),
            'end_time': DateInput(),
        }

class Invoice_Form(ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'sales_date', 'payment_date', 'payday_date', 'net_price', 'TAX', 'gross_price']
        
        widgets = {
            'date': DateInput()                      
        }

class Financial_Document(forms.Form):
        type = forms.ChoiceField(choices = Invoice_type.doc_type, disabled=True)
        doc_number = forms.CharField(max_length=100, disabled=True)
        client = forms.ModelChoiceField(queryset=Client.objects.all())
        product = forms.ModelChoiceField(queryset=Product.objects.all(), label='', widget=forms.Select(attrs={"onChange":'refresh()'}))
        unit = forms.CharField(max_length=100, disabled=True)
        sales_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        payment_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        pay_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        payment_method = forms.ChoiceField(choices = Payment_Method.pay_type)
        


