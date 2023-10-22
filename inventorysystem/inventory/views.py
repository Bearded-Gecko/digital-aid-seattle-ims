from django.shortcuts import get_object_or_404, redirect, render
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm
from django.contrib import messages
from django_pandas.io import read_frame #allows us to read models into pandas DF
import plotly
import plotly.express as px
import json #built into python, so don't need to install it
from plotly.graph_objects import Figure, Table

# Create your views here.

@login_required #requires login to access page
def inventory_list(request):
    inventories = Inventory.objects.all() #
    context = {
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request, "inventory/inventory_list.html", context = context)

@login_required
def per_product_view(request, pk): #primary key is to get each individual item
    inventory = get_object_or_404(Inventory, pk=pk) #this will filter db and return product with that pk stored in variable inventory
    context = {
        'inventory': inventory
    }

    return render(request, "inventory/per_product.html", context=context)

@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid(): #if form is valid or all forms have been filled out
            new_inventory = add_form.save(commit=False) #false b/c we don't want to automatically save to db so we can update some fields (if we added a post-calculation for example)
            new_inventory.save()
            messages.success(request, "Successfuly Added Product")
            return redirect("/inventory/")
    else:
        add_form = AddInventoryForm() #creates form without any data
        
    return render(request, "inventory/inventory_add.html", {"form": add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk) #passes in Inventory DB with key being pk
    inventory.delete() #delete
    messages.success(request, "Inventory Deleted")
    return redirect("/inventory/") 

@login_required
def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateInventoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.donor_name = updateForm.data['donor_name']
            inventory.item_type = updateForm.data['item_type']
            inventory.amount = updateForm.data['amount']
            inventory.date = updateForm.data['date']
            inventory.location = updateForm.data['location']
            inventory.save()
            messages.success(request, "Inventory Updated")
            return redirect(f"/inventory/per_product/{pk}")
    else:
        updateForm = UpdateInventoryForm(instance=inventory)
    
    context = {"form": updateForm}

    return render(request, "inventory/inventory_update.html", context=context)

@login_required
def inventory_report(request):
    inventories = Inventory.objects.all() #gets all objects from DB (models.py)
    df = read_frame(inventories) #convert objects into pandas df
    item_type_df = df.groupby(by = "item_type", as_index = False, sort = False)['amount'].sum().sort_values(by=['amount'], ascending=[False]) #group by item_type


    #TABLE
    item_type_table = Figure(data=[Table(
        header=dict(values=list(item_type_df.columns)),
        cells=dict(values=[list(item_type_df[col]) for col in item_type_df.columns]))
    ])
    item_type_table = json.dumps(item_type_table, cls = plotly.utils.PlotlyJSONEncoder)

    
    #BAR CHART
    item_type_bar = px.bar(item_type_df, 
                          x = item_type_df.item_type, 
                          y = item_type_df.amount, 
                          title = "Total Amount by Item Type"
                          )
    item_type_bar = json.dumps(item_type_bar, cls = plotly.utils.PlotlyJSONEncoder)

    context = {
        "item_type_table":item_type_table,
        "item_type_bar":item_type_bar
    }

    return render(request, "inventory/inventory_report.html", context=context)
    
@login_required
def donor_report(request):
    inventories = Inventory.objects.all() #gets all objects from DB (models.py)
    df = read_frame(inventories) #convert objects into pandas df
    donor_df = df.groupby(by = "donor_name", as_index = False, sort = False)['amount'].sum().sort_values(by=['amount'], ascending=[False])

    #TABLE
    donor_table = Figure(data=[Table(
            header=dict(values=list(donor_df.columns)),
            cells=dict(values=[list(donor_df[col]) for col in donor_df.columns]))
        ])

    donor_table = json.dumps(donor_table, cls = plotly.utils.PlotlyJSONEncoder)

    #BAR CHART  
    donor_bar = px.bar(donor_df, 
                          x = donor_df.donor_name, 
                          y = donor_df.amount, 
                          title = "Donation Amounts by Donor"
                          )
    donor_bar = json.dumps(donor_bar, cls = plotly.utils.PlotlyJSONEncoder)

    context = {
        "donor_table":donor_table,
        "donor_bar":donor_bar
    }

    return render(request, "inventory/donor_report.html", context=context)