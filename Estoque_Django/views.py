from django.shortcuts import render, HttpResponse
from .models import Products

def index(request):
    # from Products select *
    produtos = Products.objects.all()
    print(produtos)
    return render(request, 'pages/index.html')

# Create your views here.