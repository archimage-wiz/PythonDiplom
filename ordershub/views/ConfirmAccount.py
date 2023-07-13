from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from ordershub.models import ConfirmEmailToken


class ConfirmAccount(ViewSet):
    """
    Класс для подтверждения почтового адреса
    """

    # Регистрация методом POST
    def create(self, request, *args, **kwargs):

        # проверяем обязательные аргументы
        if {'email', 'token'}.issubset(request.data):

            token = ConfirmEmailToken.objects.filter(user__email=request.data['email'],
                                                     key=request.data['token']).first()
            if token:
                token.user.is_active = True
                token.user.save()
                token.delete()
                return JsonResponse({'Status': True})
            else:
                return JsonResponse({'Status': False, 'Errors': 'Неправильно указан токен или email'},
                                    json_dumps_params={'ensure_ascii': False},
                                    safe=False)
        return JsonResponse({
            'Status': False,
            'Errors': 'Не указаны все необходимые аргументы'
        },
            json_dumps_params={'ensure_ascii': False},
            safe=False)
