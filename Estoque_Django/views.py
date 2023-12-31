from django.shortcuts import render, redirect
from .models import Products, Categories
from random import randint
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def index(request):
    # from Products select *
    produtos = Products.objects.filter(user_id=request.user.id).order_by("cod")
    # print(produtos)

    for produto in produtos:
        print(f"produto.nome + produto.price")
    return render(request, "pages/index.html", {"produtos": produtos})


def stockless(request):
    produtos = Products.objects.filter(in_stock=False)
    return render(request, "pages/index.html", {"produtos": produtos})


def search_product(request):
    q = request.GET.get("q")
    if q == "":
        produtos = Products.objects.filter(name__icontains=q)
    else:
        produtos = Products.objects.filter(name__icontains=q).order_by("cod")
    return render(request, "pages/index.html", {"produtos": produtos})


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")

        unique_cod = False
        while not unique_cod:
            cod = randint(100, 10000)
            if not Products.objects.filter(cod=cod).exists():
                unique_cod = True

        category = request.POST["category"]
        picture = request.FILES.get("imagem")
        price = request.POST["price"].replace(",", ".")
        description = request.POST.get("description")
        qtd = request.POST["qtd"]
        discount = request.POST.get("discount")
        created_at = datetime.now()

        in_stock = True
        if int(qtd) == 0:
            in_stock = False

        Products.objects.create(
            user_id=request.user.id,
            name=name,
            cod=cod,
            category_id=category,
            picture=picture,
            price=price,
            description=description,
            qtd=qtd,
            discount=discount,
            created_at=created_at,
            in_stock=in_stock,
        )

        return redirect("home")
    else:
        categories = Categories.objects.all()
        return render(request, "pages/add_product.html", {"categories": categories})


def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, "pages/product_detail.html", {"product": product})


def delete_product(request, id):
    product = Products.objects.get(id=id).delete()
    return redirect("home")


def sell_product(request, id):
    product = Products.objects.get(id=id)
    if int(product.qtd) == 0:
        product.in_stock = False
        product.save()
        messages.success(request, "Este produto não possui estoque!")
    else:
        product.qtd -= 1
        product.save()
        messages.success(request, "Produto vendido com sucesso!")
    return redirect("product-detail", id=id)


# def cancel_product():
# if request.method == "POST":
# Limpar os campos do formulário aqui
# Por exemplo, você pode criar um formulário vazio e renderizá-lo novamente
# return redirect("add-product")
