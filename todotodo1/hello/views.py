from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from datetime import date
from . import models
# Create your views here.
def index(request):
    return HttpResponse("<h1>hello</h1>")


def getAllTodos(request):
    todos = serializers.serialize('json', models.Todo.objects.all())

    return HttpResponse(todos, content_type='application/json')
#get by id 
def getTodo(request,id):
    #get me the Todo with that id

def deleteTodo(request,id):
    #

def update(request,id):
    #

def update(request,id):
    #


def say_hello(request,name):
    return HttpResponse("<h1>hello "+name+"</h1>")


def isItAid(req):
    today = str(date.today())
    print(today)
    if today =="'2024-06-16'" :
        return HttpResponse("Aidek mabrouk !")
    return HttpResponse("Arjaa ghodwa ! ")
    
