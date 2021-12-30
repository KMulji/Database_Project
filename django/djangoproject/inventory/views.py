from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Order, PO


def index(request):
    context = {"Orders": Order.objects.order_by('DatePlaced')[:10]}
    return render(request, 'index2.html', context)


def index2(request,id):
    products_list = PO.objects.filter(Order=id)
    total_price = 0
    for i in range(len(products_list)):
        total_price += products_list[i].Product.SellingPrice * products_list[i].Quantity

    context = {"Pos": PO.objects.filter(Order__id=id), "Order":Order.objects.get(id=id), "GrandTotal" : total_price}

    return render(request, 'index3.html', context)
