from django.http import HttpResponse, Http404
from django.shortcuts import render

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    return HttpResponse("product {}".format(product_id))

def available_products(request):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    return HttpResponse("View not implemented!")
