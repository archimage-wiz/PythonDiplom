from rest_framework.viewsets import ModelViewSet

from ordershub.models import Shop
from ordershub.serializers import ShopSerializer


class ViewShop(ModelViewSet):
    """
    Класс для просмотра магазинов.
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer
    http_method_names = ['get']
