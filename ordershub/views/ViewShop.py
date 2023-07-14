from rest_framework.generics import ListAPIView

from ordershub.models import Shop
from ordershub.serializers import ShopSerializer


class ViewShop(ListAPIView):
    """
    Класс для просмотра магазинов.
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer
    http_method_names = ['get']
