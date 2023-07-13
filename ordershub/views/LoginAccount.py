from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ViewSet


class LoginAccount(ViewSet):
    """
    Класс для авторизации пользователей
    """

    # Авторизация методом POST
    def create(self, request, *args, **kwargs):

        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)
                    return JsonResponse({'Status': True, 'Token': token.key})
            return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})
        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
