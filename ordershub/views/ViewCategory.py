from rest_framework.generics import ListAPIView

from ordershub.models import Category
from ordershub.serializers import ProductSerializer


class ViewCategory(ListAPIView):
    """
    Класс для просмотра категорий
    """
    queryset = Category.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
