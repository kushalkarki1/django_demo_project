from django.http import HttpResponse
from django.shortcuts import render
from demo.models import Product

def home(request):
    # return HttpResponse("<h1>Django Success!</h1>")
    products = Product.objects.all()
    data = {"products": products}
    return render(request, "home.html", data)