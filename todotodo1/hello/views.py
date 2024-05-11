from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from http import HTTPStatus
import json

from datetime import date
from . import models
# Create your views here.
def index(request):
    return HttpResponse("<h1>hello</h1>")

def getAllTodos(request):
    todos = serializers.serialize('json', models.Todo.objects.all())
    todos
    return HttpResponse(todos, content_type='application/json')
#get by id 
def getTodoAndDelete(request,todo_id):
    if request.method=="GET":
        try:
            todo = serializers.serialize('json',  [models.Todo.objects.get(id=todo_id)])
            print(todo)
        except :
            return HttpResponse("No item with that id ",status=HTTPStatus.NOT_FOUND)
        return HttpResponse(todo)
def createTodo(request):
    if request.method=="POST":
        data = json.loads(request.body)
        try :
            text = data["text"]
            newTodo = models.Todo(text=text,done=False)
            newTodo.save()
        except : 
           return HttpResponse("missing text to create todo",status=HTTPStatus.BAD_REQUEST) 
    
        return HttpResponse(newTodo,status=HTTPStatus.CREATED)


        

def login(request):
    # data validation 
    
    data = json.loads(request.body)
    try :
        email = data["email"]
        password = data["password"]
    except : 
        return HttpResponse("missing email or password",status=HTTPStatus.BAD_REQUEST) 
    
    return HttpResponse(str({"email":email,"password":password}))

def login(request):
    # data validation 
    
    data = json.loads(request.body)
    try :
        email = data["email"]
        password = data["password"]
    except : 
        return HttpResponse("missing email or password",status=HTTPStatus.BAD_REQUEST) 
    
    return HttpResponse(str({"email":email,"password":password}))

"""def deleteTodo(request,id):
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
    return HttpResponse("Arjaa ghodwa ! ")"""