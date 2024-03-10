from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from phone.forms import CreateUserForm, LoginUserForm
from phone.models import ItemDetails, Items, Cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    request.session["cart_count"] = request.session.get("cart_count", 0)
    return HttpResponse(template.render({"request": request}))


def show_phone(request):
    template = loader.get_template("showPhone.html")
    phone = ItemDetails.objects.select_related("itemsid")
    return HttpResponse(template.render({"phone": phone, "request": request}))


def details(request, id):
    template = loader.get_template("details.html")
    phone = ItemDetails.objects.select_related("itemsid").filter(itemsid=id)
    similar_phone = ItemDetails.objects.exclude(itemsid=id)
    context = {"phone": phone, "request": request, "similar_phone": similar_phone}
    return HttpResponse(template.render(context=context))


@csrf_exempt
def auth_register(request):
    template = loader.get_template("auth_register.html")
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auth_login")
    context = {"registerform": form, "request": request}
    return HttpResponse(template.render(context=context))


@csrf_exempt
def auth_login(request):
    form = LoginUserForm()
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    count = Cart.objects.filter(id_user=request.user.id).count()
                    request.session["cart_count"] = count
                    return render(request, "index.html")

    context = {"form": form}
    return render(request, "auth_login.html", context)


@csrf_exempt
def auth_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")


@login_required(login_url="auth_login")
def add_to_cart(request, product_id):
    current_user = request.user
    discount = 2
    phone = ItemDetails.objects.select_related("itemsid").filter(itemsid=product_id)
    for item in phone:
        net = float("{:.2f}".format((item.total * (item.tax + 1)) - discount))
    cart_data = Cart(
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
    return redirect("/showphone/")


@login_required(login_url="auth_login")
def checkout(request):
    try:
        template = loader.get_template("checkout.html")
        current_user_id = request.user.id
        cart = Cart.objects.all().filter(id_user=current_user_id).first()
        product = Items.objects.get(id=cart.id_product)
        context = {"cart": cart, "productname": product, "request": request}
    except:
        return HttpResponse("<h1>Your Cart is Empty!!</h1>")
    return HttpResponse(template.render(context=context))


@login_required(login_url="auth_login")
def buy_now(request, product_id):
    try:
        template = loader.get_template("checkout.html")
        current_user_id = request.user.id
        cart = Cart.objects.all().filter(id_user=current_user_id, id_product=product_id).first()
        product = Items.objects.get(id=cart.id_product)
        context = {"cart": cart, "productname": product, "request": request}
    except:
        return HttpResponse("<h1>Add the Product to your Cart First</h1>")
    return HttpResponse(template.render(context=context))
