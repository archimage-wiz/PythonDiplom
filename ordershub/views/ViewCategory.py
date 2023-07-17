from rest_framework.viewsets import ModelViewSet

from ordershub.models import Category
from ordershub.serializers import ProductSerializer


class ViewCategory(ModelViewSet):
    """
    Класс для просмотра категорий
    """
    queryset = Category.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
