from django.shortcuts import render
from django.http import HttpResponse

info = {'имя': 'Анастасия', 'отчество':'Александровна', 'фамилия':'Дудченко', 'телефон':'8-923-600-03-03', 'email':'andud@mail.ru'}
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    text = """<h1>"Изучаем django"</h1>
              <strong>Автор</strong>: <i>Дудченко А.А.</i>
           """
    return HttpResponse(text)


def about(request):
    text = f"""Имя: <b>{info['имя']}</b><br>
            Отчество: <b>{info['отчество']}</b><br>
            Фамилия: <b>{info['фамилия']}</b><br>
            телефон: <b>{info['телефон']}</b><br>
            email: <b>{info['email']}<br>"""
    return HttpResponse (text)

def get_item(request, id):

    for i in range(len(items)):
        if items[i]["id"] == id:
            return HttpResponse(f'<b>Название:</b> {items[i]["name"]}, <b>Количество:</b> {items[i]["quantity"]}<br><a href = "../items">назад к списку товаров</a>')
    
    return HttpResponse(f'Товар с id={id} не найден<br><a href = "../items">назад к списку товаров</a>')

def get_items(request):

    text = "<ol>"

    for i in range(len(items)):
        text+=f'<li><a href = "item/{items[i]["id"]}">{items[i]["name"]}</a></li>'

    text+="</ol>"

    return HttpResponse(text)

    