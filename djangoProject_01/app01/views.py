
# Create your views here.
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("wellcome")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")