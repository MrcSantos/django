from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import seller_form
from .forms import product_form


def index(request):
    return HttpResponse("Welcome to the black market site!<br><a href='products/'>Visita i nostri prodotti!</a>")


def products(request):
    return HttpResponse("You're seeing all products.<br><a href='http://localhost:8000/product/1'>Prodotto numero 1</a><br><a href='http://localhost:8000/product/2'>Prodotto numero 2</a><br><a href='http://localhost:8000/product/3'>Prodotto numero 3</a><br><a href='http://localhost:8000/product/4'>Prodotto numero 4</a><br><a href='http://localhost:8000/product/5'>Prodotto numero 5</a>")


def product(request, id_prod):
    return HttpResponse("You're seeing the product #%s" % id_prod)


def seller(request, id_seller):
    return HttpResponse("You're seeing the seller #%s" % id_seller)


def new_seller(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = seller_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = seller_form()

    return render(request, 'name.html', {'form': form})
