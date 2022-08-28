from datetime import date, datetime
from itertools import product
from math import prod
from time import timezone
from tkinter.messagebox import NO
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Unit, Client, Project, Invoice, Unit
from django.contrib.auth.decorators import login_required, permission_required
from .forms import Financial_Document, Project_Form, Client_Form, Product_Form, Invoice_Form


# Create your views here.


@login_required
def Warehouse(request):
    products = Product.objects.all()
    warehouse_value = 0.00

    for i in products:
        price = i.price * i.quantity
        warehouse_value += price
        
    round(warehouse_value, 2)
    form_new_product = Product_Form(request.POST or None)
    if form_new_product.is_valid():
        form_new_product.save()
        return redirect(Warehouse)
    return render(request, 'warehouse.html',
                      {'form': form_new_product, 'products': products, 'warehouse_value': warehouse_value,
                       'units': Unit.unit})

@login_required
def Mainsite(request):

    products = Product.objects.all()   
    warehouse_value = 0.0
    for i in products:
        price = i.price * i.quantity
        warehouse_value += price

    projects = Project.objects.all()
    project_count = 0
    budget_summary = 0.0
    income_summary = 0.0
    for i in projects:
        project_count = projects.count()
        budget_summary += i.budget 


    return render(request, 'main_site.html', {'products': products, 'warehouse_value': round(warehouse_value, 2), 'projects_number': project_count, 'budget_summary': budget_summary, 'income_summary': income_summary})

def Registration(request):
    return render(request, 'register.html')

@login_required
def Edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    product_form = Product_Form(request.POST or None, instance=product)

    if(product_form.is_valid()):
        product = product_form.save()
        product.save()
        return redirect(Warehouse)

    return render(request, 'Edit_product.html', {'form': product_form})

@login_required
def Remove_produkt(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.delete()
        return redirect(Warehouse)

    return render(request, 'confirmation.html', {'product': product})

@login_required
def Clients(request):
    client = Client.objects.all()
    form_client = Client_Form(request.POST or None)
    if form_client.is_valid():
        form_client.save()
        return redirect(Clients)
    return render(request, 'clients.html', {'form': Client_Form ,'client': client})

@login_required
def Edit_client(request, id):
    client = get_object_or_404(Client, pk=id)

    client_form = Client_Form(request.POST or None, instance=client)

    if(client_form.is_valid()):
        client_form.save()

        return redirect(Clients)

    return render(request, 'edit_client.html', {'form': client_form})

@login_required
def Remove_client(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == "POST":
        client.delete()
        return redirect(Clients)

    return render(request, 'confirmation.html', {'client': client})

@login_required
def Projects(request):
    project = Project.objects.all()
    form_project = Project_Form(request.POST or None)
    if form_project.is_valid():
        form_project.save()
        return redirect(Projects)
    return render(request, 'projects.html', {'form': Project_Form ,'project': project})

@login_required
def Edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    project_Form = Project_Form(request.POST or None, instance=project)

    delta = project.scheduled_end_time - date.today()
    days_to_end = delta.days
    if project.end_time != None and project.end_time != "":
        delta = project.scheduled_end_time - project.end_time
        days_to_end = delta.days
        project_completed = True
    else:
        project_completed = False
    if(project_Form.is_valid()):
        project_Form.save()

        return redirect(Edit_project, project.pk)

    return render(request, 'edit_project.html', {'form': project_Form, 'project_id':project.pk, 'project_name': project.name, 'client': project.client, 'street': project.street, 'house_number': project.house_number, 'postal_code': project.postal_code, 'town': project.town, 'start_time': project.start_time,
                                                   'scheduled_end_time': project.scheduled_end_time, 'end_time': project.end_time, 'days_to_end': days_to_end,
                                                   'description': project.description, 'budget': project.budget, 'project_completed': project_completed})

@login_required
def Financial_Management(request):
    invoice = Invoice.objects.all()
    invoice_number = ""
    if not invoice :            
        i_number = 1
        print(i_number)
        date = datetime.now()
        month = date.strftime("%m") 
        year = date.strftime("%Y")
        invoice_number = f"FV/{i_number}/{month}/{year}"
        invoice_number = str(invoice_number)
    else:
        for i in invoice: 
            i_number = i.number[3:4] 
            i_number = int(i_number) + 1
            print(i_number)
            date = datetime.now()
            month = date.strftime("%m")
            year = date.strftime("%Y")
            invoice_number = f"FV/{i_number}/{month}/{year}"
            invoice_number = str(invoice_number)

    

    client = Client.objects.all()
    id_client = ""
    invoice_form = Invoice_Form(request.POST or None)
    if invoice_form.is_valid():
        obj = invoice_form.save(commit=False)
        obj.number = str(invoice_number)
        obj.save()
        return redirect(Financial_Management)
    return render(request, 'Financial_Management.html', {'form': invoice_form, 'invoice': invoice, 'client': client, 'id_client': id_client, 'invoice_number': invoice_number})

@login_required
def Invoice__(request):
    client = Client.objects.all()
    product = Product.objects.all()
    inv = Invoice.objects.all()
    invoice_number = ""
    
    if not inv :            
        i_number = 1
        print(i_number)
        date = datetime.now()
        month = date.strftime("%m") 
        year = date.strftime("%Y")
        invoice_number = f"FV/{i_number}/{month}/{year}"
        invoice_number = str(invoice_number)
    else:
        for i in inv: 
            i_number = i.number[3:4] 
            i_number = int(i_number) + 1
            print(i_number)
            date = datetime.now()
            month = date.strftime("%m")
            year = date.strftime("%Y")
            invoice_number = f"FV/{i_number}/{month}/{year}"
            invoice_number = str(invoice_number)



    initial_dict = {
        'doc_number': invoice_number,
        'type': 'VAT Sales Invoice',
        'unit': Product.unit,
    }
    
    id_client = ""
    invoice_form = Financial_Document(request.POST or None, initial= initial_dict)
    if invoice_form.is_valid():
        obj = invoice_form.save(commit=False)
        obj.number = str(invoice_number)
        obj.save()
        return redirect(Invoice__)
    return render(request, 'invoice.html', {'form': invoice_form, 'invoice': inv, 'client': client, 'id_client': id_client, 'invoice_number': invoice_number, 'product': product})

def my_view_function(request):

    val1 = request.POST['key1']
    response = {
        'key2' : 'val2',
    }

    return JsonResponse(response)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def checkProduct(request):
    if is_ajax(request=request) and request.method == "GET":
        id_product = request.GET.get("id_product", None)
        amount = request.GET.get("Amount", None)
        amount = float(amount)
        if Product.objects.filter(pk = id_product).exists():
            product = get_object_or_404(Product, pk=id_product)
            TAX = 0.23
            gross_price = amount * product.price
            gross_price = gross_price + (gross_price * TAX)
            print(gross_price)
            
            return JsonResponse({"valid":True, "name": product.name, "unit": product.unit, "in_stock": product.quantity, "price": product.price, "TAX": TAX, "gross_Price": gross_price}, status = 200)
        else:
            print(id_product)
            return JsonResponse({"valid":False}, status = 200)
            

    return JsonResponse({}, status = 400)
    