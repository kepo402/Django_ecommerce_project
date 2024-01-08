
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from .models import Cart, Order
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def addtocart(request, slug):
    Product = apps.get_model('product', 'Product')
    try:
        item = get_object_or_404(Product, slug=slug)
    except Product.DoesNotExist:
        messages.error(request, 'Product not found')
        return redirect('home')
    if not  request.user.is_authenticated:
        messages.error(request, 'Please log in to add items to your cart')
        return redirect('mainapp:home')
    quantity = int(request.GET.get('quantity', 1))        
    order_item, created = Cart.objects.get_or_create(
        item= item,
        user = request.user,
        
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item in Order.orderitems.through.objects.filter(order=order):
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated in your cart")
        else:
            order.orderitems.add(order_item)
            messages.info(request,  "This item was added to your cart")
    else:
        order = Order.objects.create(user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect('mainapp:home')                

    
