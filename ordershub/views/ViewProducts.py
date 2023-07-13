from django.db.models import Q
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from ordershub.models import Product, ProductInfo
from ordershub.serializers import ProductInfoSerializer, ProductSerializer


class ViewProducts(ViewSet):
    """
    Класс для поиска товаров.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

    def list(self, request):
        shop_id = request.query_params.get('shop_id')
        category_id = request.query_params.get('category_id')
        query = Q(shop__state=True)
        query = query & Q(shop_id=shop_id) if shop_id else query
        query = query & Q(product__category_id=category_id) if category_id else query
        queryset = ProductInfo.objects.filter(query) \
            .select_related('shop', 'product__category') \
            .prefetch_related('product_parameters__parameter').distinct()
        serializer = ProductInfoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False)
