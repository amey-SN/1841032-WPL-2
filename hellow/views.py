from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, This is  Amey from T2 Batch and my PRN is 1841032</h1>")

# Create your views here.
