from faulthandler import disable
from django.db import models
from django.utils import timezone





class Unit(models.Model):
    szt = 'szt'
    m = 'm'
    km = 'km'
    op = 'op'
    opz = 'opz'
    unit = [
        (szt, 'szt'),
        (m, 'm'),
        (km, 'km'),
        (op, 'op'),
        (opz, 'opz')
    ]

class Category(models.Model):
    wires = 'Wires'   
    cable_holders = 'Cable Holders'
    building_materials = 'Building Materials'
    tools = 'tools'
    category = [
        (wires, 'Wires'),
        (cable_holders, 'Cable Holders'),
        (building_materials, 'Building Materials'),
        (tools, 'Tools'),
    ]

class Invoice_type(models.Model):
    receipt_sales = 'Sales Receipt'
    retail_sales_invoice = 'Retail Sales Invoice'
    VAT_sales_invoice = 'VAT Sales Invoice'
    receipt_purchase = 'Purchase Receipt'
    retail_purchase_invoice = 'Retail Purchase Invoice'
    VAT_purchase_invoice = 'VAT Purchase Invoice'
    doc_type = [
        (receipt_sales, 'Receipt Sales'),
        (retail_sales_invoice, 'Retail Sales Invoice'),
        (VAT_sales_invoice, 'VAT Sales Invoice'),
        (receipt_purchase, 'Receipt Purchase'),
        (retail_purchase_invoice, 'Retail Purchase Invoice'),
        (VAT_purchase_invoice, 'VAT Purchase Invoice'),
    ]

class Payment_Method(models.Model):
    cash = 'Cash'
    Checks = 'Checks'
    debit_cards = 'Debit cards'
    electronic_bank_transfers = 'Electronic bank transfers'
    pay_type = [
        (cash, 'Cash'),
        (Checks, 'Checks'),
        (debit_cards, 'Debit cards'),
        (electronic_bank_transfers, 'Electronic bank transfers'),
    ]

class payment_check(models.Model):
    paid = 'paid'
    not_paid = 'not paid'
    payment_choise = [
        (paid, 'paid'),
        (not_paid, 'Not Paid'),
    ]

class Product(models.Model):
    name = models.CharField(max_length=260, blank=False, null=False, unique=True)
    unit = models.CharField(max_length=3, choices=Unit.unit, default=Unit.szt)
    quantity = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    price = models.FloatField(blank=False, null=False, default=0)
    category = models.CharField(max_length=100, choices=Category.category, default=Category.building_materials)
    def __str__(self):
        return str(self.name)

class Client(models.Model):
    company_name = models.CharField(max_length=300, blank=True, unique=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    house_number = models.PositiveSmallIntegerField(blank=True, null=True)
    postal_code = models.PositiveSmallIntegerField(blank=False, null=False)
    town = models.CharField(max_length=30, blank=False, null=False)   
    phone_numer_1 = models.PositiveSmallIntegerField(blank=False, null=False)
    phone_number_2 = models.PositiveSmallIntegerField(blank=True, null=True)
    TIN = models.PositiveSmallIntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(max_length=260, blank=True, null=True, unique=True)
    def __str__(self):
        tin = str(self.TIN)
        return str(self.company_name +", "+ self.name + " " + self.lastname + " " + tin).replace('None', '')

class Project(models.Model):
    name = models.CharField(max_length=260, blank=False, null=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_time = models.DateField(blank=False, null=False)
    scheduled_end_time = models.DateField(blank=False, null=False)
    end_time = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=260, blank=True, null=True)
    street = models.CharField(max_length=260, blank=False, null=False)
    house_number = models.PositiveSmallIntegerField(blank=False, null=False)
    postal_code = models.PositiveSmallIntegerField(blank=False, null=False, default=00000)
    town = models.CharField(max_length=260, blank=False, null=False)
    budget = models.FloatField(blank=True, default=0.00)

class Invoice(models.Model):
    number = models.CharField(max_length=260, blank=False, null=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sales_date = models.DateField(blank=False, null=False, default=timezone.now)
    payment_date = models.DateField(blank=False, null=False, default=timezone.now)
    payday_date = models.DateField(blank=False, null=False, default=timezone.now)
    net_price = models.FloatField(blank=False, null=True)
    TAX = models.FloatField(blank=False, null=True)
    gross_price = models.FloatField(blank=False, null=True)
    type_of_document = models.CharField(max_length=30, choices=Invoice_type.doc_type, default=Invoice_type.VAT_purchase_invoice)
    payment_status = models.CharField(max_length=20,choices=payment_check.payment_choise, default=payment_check.not_paid)
