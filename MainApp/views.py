from django.shortcuts import render
from django.http import HttpResponse, Http404

info = {'имя': 'Анастасия', 'отчество':'Александровна', 'фамилия':'Дудченко', 'телефон':'8-923-600-03-03', 'email':'andud@mail.ru'}
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    return render(request, "index.html")


def about(request):
    return render (request, "about.html", {"info": info})

def get_item(request, id):
    for i in range(len(items)):
        if items[i]["id"] == id:
            return render(request, "item.html", {"name":items[i]["name"], "count": items[i]["quantity"]})

def get_items(request):
    return  render(request, "items_list.html",  {"items":items})

    