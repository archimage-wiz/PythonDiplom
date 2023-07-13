from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from ordershub.models import User


class UserAuth(ViewSet):
    """
    Класс для проверки и получения токена
    """
    queryset = User.objects.all()

    @action(detail=False, methods=['post'], url_path='auth')
    def auth(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if not user or not user.check_password(request.data['password']):
            return JsonResponse({'error': 'Error email or password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
        token2 = Token.objects.get_or_create(user=user)
        return JsonResponse({
            "Status": "ok",
            "token": str(token2[0])
        })

    @action(detail=False, methods=['post'], url_path='test_token')
    def test(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        return JsonResponse({
            "Status": "Login ok",
        })
