from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required()
def product(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()
    context = {
        'form': form,
        'products':products
    }
    return render(request,"products/products.html",context)
@login_required()
def delete_product(request,id):
    Product.objects.filter(id=id).delete()
    messages.success(request,"Product Delete")
    return redirect("products")
@login_required()
def update_product(request,id):
    products = Product.objects.filter(id=id).first()
    if request.method == "POST":
        form = ProductForm(request.POST or None,instance=products)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=products)

    context = {
        'products':products,
        'form': form,
    }
    return render(request,'products/edit.html',context)



