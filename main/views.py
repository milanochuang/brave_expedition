from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Features, Questions
from .forms import CreateNewList, CreateNewFeatures

# Create your views here.
def hello_django(response):
    return render(response,"main/hello_django.html",{})

def background(response):
    return render(response,"main/background.html",{})

def maps(response):
    if response.method == "POST":
        if response.POST.get("map1"):
            return HttpResponseRedirect("/question")
    else:    
        return render(response,"main/maps.html",{})


def question(response):
    
    return render(response,"main/question.html",{})

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            if response.POST.get("c37") == "clicked":
                if response.POST.get("c38") == "clicked":
                    if response.POST.get("c39") != "clicked":
                        return HttpResponseRedirect("correct")
                    else:
                        return HttpResponseRedirect("/incorrect")
                else:
                    return HttpResponseRedirect("/incorrect")
            else:
                return HttpResponseRedirect("incorrect")            


    return render(response, "main/list.html",{"ls":ls})


def correct(response):
    return render(response, "main/correct.html",{})

def incorrect(response):
    if response.POST.get("tryagain"):
        return HttpResponseRedirect("22#")
    else:
        return render(response,"main/incorrect.html",{})

        
def home(response):
    return render(response, "main/home.html",{})

def stuff(response):
    return render(response, "main/stuff.html",{}) 

