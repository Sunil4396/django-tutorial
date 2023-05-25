from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    prd=Product.objects.all()
    return render(request,'curdapp/index.html',{'prd':prd})
def insert(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request,'curdapp/insert.html',{'form':form})

def delete(request,id):
    prd=Product.objects.get(id=id)
    prd.delete()
    return HttpResponseRedirect('/')


