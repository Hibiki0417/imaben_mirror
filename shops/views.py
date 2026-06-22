from django.http import HttpResponse


def shop_list(request):
    return HttpResponse("いま弁 店舗一覧ページ")