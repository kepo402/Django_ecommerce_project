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
    
