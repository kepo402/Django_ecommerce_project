from django.shortcuts import render, get_object_or_404
from product.models import Product
from  .models import Cart, Order

# Create your views here.
def addtocart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item= item,
        user = request.user,
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item.filter(slug=slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated in your cart")
        else:
            order.items.add(order_item)
            messages.info(request,  "This item was added to your cart")
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect('',slug=slug)                

    
