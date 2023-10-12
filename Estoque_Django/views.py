from django.shortcuts import render, HttpResponse

def index(REQUEST):
    return HttpResponse('Estou no Django')

# Create your views here.
