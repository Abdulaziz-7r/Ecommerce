from django.shortcuts import render
from django.http import JsonResponse
from phone.models import Items, ItemDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def get_all_items_list(request):
    phone = Items.objects.all()  # get all items
    phone_list = list(phone.values())
    return Response(phone_list)

@api_view(["GET"])
def get_all_items_details_list(request):
    phone = ItemDetails.objects.select_related("itemsid").all()  # get all items details
    list1 = []
    for item in phone:
        getitems = {
            "id": item.id,
            "name": item.itemsid.name,
            "color": item.color,
            "price": item.price,
            "qty": item.qty,
            "tax": item.tax,
            "total": item.total,
            "qty": item.qty
        }
        list1.append(getitems)
    # phone_list = list(phone.values())
    return JsonResponse({"phone": list1})


def get_all_items_details_by_id(request,id):
    phone = ItemDetails.objects.select_related("itemsid").filter(id=id)  # get items details by id
    list1 = []
    for item in phone:
        getitems = {
            "id": item.id,
            "name": item.itemsid.name,
            "color": item.color,
            "price": item.price,
            "qty": item.qty,
            "tax": item.tax,
            "total": item.total,
            "qty": item.qty,
        }
        list1.append(getitems)
    # phone_list = list(phone.values())
    return JsonResponse({"phone": list1})
