from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Item, Author


def home(request):
    return render(request, "index.html")


def about(request):
    return render (request, "about.html", {"author": Author.objects.get(id=1)})

def get_item(request, id_i):
    return render(request, "item.html", {"item": Item.objects.get(id=id_i)})

def get_items(request):
    return  render(request, "items_list.html",  {"items": Item.objects.all()})

    