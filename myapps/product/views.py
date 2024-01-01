from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  ListView
from .models import Product, Category


def Createdummy(request):
    category = Category.objects.create(title='clothing', primarycategory=True)

    product1 = Product.objects.create(
    mainimage = 'images/product1.jpg',
    name = 'Awesome Tshirt',
    slug  = 'awesome-tshirt',
    category = category,
    previewtext = 'This is a cool tshirt',
    detailtext = 'this shirt is made of 100% cotton',
    price = 29.99,
)
    return HttpResponse('dummy product created successfully') 

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'product/home.html'
