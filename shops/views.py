from django.shortcuts import render, get_object_or_404
from .models import Shop


def shop_list(request):
    shops = Shop.objects.all()
    return render(request, "shops/shop_list.html", {"shops": shops})

def shop_detail(request,pk):
    shop = get_object_or_404(Shop,pk=pk)
    return render(request, "shops/shop_detail.html", {"shop":shop} )