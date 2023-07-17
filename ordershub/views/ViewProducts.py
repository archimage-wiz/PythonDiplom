from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet

from ordershub.models import ProductInfo
from ordershub.serializers import ProductInfoSerializer


class ViewProducts(ViewSet):
    """
    Класс для поиска товаров.
    """
    http_method_names = ['get']

    def list(self, request):
        shop_id = request.query_params.get('shop_id')
        category_id = request.query_params.get('category_id')
        if not shop_id and not category_id:
            return JsonResponse({"Status": "error",
                                 "detail": "Shop or Category must be provided."},
                                status=status.HTTP_400_BAD_REQUEST)
        query = Q(shop__state=True)
        query = query & Q(shop_id=shop_id) if shop_id else query
        query = query & Q(product__category_id=category_id) if category_id else query
        queryset = ProductInfo.objects.filter(query) \
            .select_related('shop', 'product__category') \
            .prefetch_related('product_parameters__parameter').distinct()
        serializer = ProductInfoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False)
