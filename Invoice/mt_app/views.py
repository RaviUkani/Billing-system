from django.db.models import F
from django.shortcuts import render, redirect
from .models import Customer, Order, Item
from django.db.models import Sum
from .forms import CustomerForm, OrderForm, ItemForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'mt_app/customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'mt_app/order_list.html', {'orders': orders})

def item_list(request):     
    items = Item.objects.all()
    return render(request, 'mt_app/item_list.html', {'items': items})

def home(request):
    return render(request, 'mt_app/home.html')

def invoice(request,pk):
    customer = Customer.objects.get(id = pk)
    order = Order.objects.get(id =pk)
    item =Item.objects.filter(order= order)
    context = {
        'customer':customer,
        'order':order,
        'item':item,
        'total':item.aggregate(total_price=Sum('item_price'))['total_price']
    }
    return render(request, 'mt_app/invoice.html',context)

def customer_input(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_saved')
    else:
        form = CustomerForm()
        return render(request, 'mt_app/customer_input.html', {'form': form})

def order_input(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_saved')
    else:
        form = OrderForm()
        return render(request, 'mt_app/order_input.html', {'form': form})


def item_input(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_saved')
    else:
        form = ItemForm()
        return render(request, 'mt_app/item_input.html', {'form': form})
