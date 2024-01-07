from django.urls import path
from . import views

urlpatterns = [
    path('addtocart/<slug>/', views.addtocart, name='addtocart'),

]