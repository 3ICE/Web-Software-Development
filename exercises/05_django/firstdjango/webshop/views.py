from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    #p = Product.objects.filter(id__exact=product_id)
    try:
        p = Product.objects.get(id=int(product_id))
        return render_to_response('webshop/product_view.html',{'product': p})
    except Product.DoesNotExist:
        raise Http404("Not found")

def available_products(request):
    return render_to_response('webshop/product_list.html',{'products': Product.objects.filter(quantity__gt=0)})
    #return HttpResponse("View not implemented!")
		