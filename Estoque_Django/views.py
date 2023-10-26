from django.shortcuts import render, redirect
from .models import Products, Categories
from random import randint
from datetime import datetime

def index(request):
    # from Products select *
    produtos = Products.objects.all()
    # print(produtos)

    for produto in produtos:
        print(f'produto.nome + produto.price')
    return render(request, 'pages/index.html', {'produtos':produtos})

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cod = randint(100, 10000) #fazer validação posteriormente
        category = request.POST['category']
        picture = request.FILES.get('picture')
        price = request.POST['price']
        description = request.POST.get('description')
        qtd = request.POST['qtd']
        discount = request.POST.get('discount')
        created_at = datetime.now()
        in_stock = True #fazer validação posteriormente com a qtd

        Products.objects.create(
            name = name, cod=cod, category_id=category, picture=picture, price=price, description=description, qtd=qtd, 
            discount= discount, created_at=created_at, in_stock=in_stock
        )

        return redirect('home')
    else:
        categories = Categories.objects.all()
        return render(request, 'pages/add-product.html', {'categories': categories})

def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product_detail.html', {'product' : product})

def delete_product(request, id):
    product = Products.objects.get(id=id).delete()
    return redirect('home')


