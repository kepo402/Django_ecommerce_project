from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import  ListView
from .models import Product, Category


class LoginView(View):
    template_name = 'product/login.html'

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'product/home.html'
