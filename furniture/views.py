from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from phone.forms import CreateUserForm, LoginUserForm

from furniture.models import Furniture, FurnitureDetails, CartFurniture
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_furniture(request):
    template = loader.get_template("show_furniture.html")
    furniture = FurnitureDetails.objects.select_related("itemsid")
    return HttpResponse(template.render({"furniture": furniture, "request": request}))


def furniture_details(request, id):
    template = loader.get_template("furniture_details.html")
    furniture = FurnitureDetails.objects.select_related("itemsid").filter(itemsid=id)
    similar_furniture = FurnitureDetails.objects.exclude(itemsid=id)
    context = {
        "furniture": furniture,
        "request": request,
        "similar_furniture": similar_furniture,
    }
    return HttpResponse(template.render(context=context))


@login_required(login_url="auth_login")
def add_to_cart_furniture(request, product_id):
    current_user = request.user
    discount = 50
    furniture = FurnitureDetails.objects.select_related("itemsid").filter(
        itemsid=product_id
    )
    for item in furniture:
        net = float("{:.2f}".format((item.total * (item.tax + 1)) - discount))
    cart_data = CartFurniture(
        id_product=item.itemsid.id,
        id_user=current_user.id,
        price=item.price,
        qty=item.qty,
        tax=item.tax,
        total=item.total,
        discount=discount,
        net=net,
        status=False,
    )
    cart_data.save()
    request.session["cart_count"] = int(request.session["cart_count"]) + 1
    return redirect("/show_furniture/")


@login_required(login_url="auth_login")
def buy_now_furniture(request, product_id):
    try:
        template = loader.get_template("checkout.html")
        current_user_id = request.user.id
        cart = (
            CartFurniture.objects.all()
            .filter(id_user=current_user_id, id_product=product_id)
            .first()
        )
        product = Furniture.objects.get(id=cart.id_product)
        context = {"cart": cart, "productname": product, "request": request}
    except:
        return HttpResponse("<h1>Add the Product to your Cart First</h1>")
    return HttpResponse(template.render(context=context))


@login_required(login_url="auth_login")
def checkout_furniture(request):
    try:
        template = loader.get_template("checkout.html")
        current_user_id = request.user.id
        cart = CartFurniture.objects.all().filter(id_user=current_user_id).first()
        product = Furniture.objects.get(id=cart.id_product)
        context = {"cart": cart, "productname": product, "request": request}
    except:
        return HttpResponse("<h1>Your Cart is Empty!!</h1>")
    return HttpResponse(template.render(context=context))
