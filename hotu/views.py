from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요!'.format(name, age))

def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1> Hosung Tour </h1>
    <p> {name} </p>
    <p> Welcome to hosung tour </p>
    '''.format(name=name))
