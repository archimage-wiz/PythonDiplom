from django.contrib import admin
from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from ordershub.views.AccountDetails import AccountDetails
from ordershub.views.ConfirmAccount import ConfirmAccount
from ordershub.views.ContactView import ContactView
from ordershub.views.LoginAccount import LoginAccount
from ordershub.views.PartnerOrders import PartnerOrders
from ordershub.views.PartnerState import PartnerState
from ordershub.views.PartnerUpdate import PartnerUpdate
from ordershub.views.RegisterAccount import RegisterAccount
from ordershub.views.UserAuth import UserAuth
from ordershub.views.ViewBasket import ViewBasket
from ordershub.views.ViewCategory import ViewCategory
from ordershub.views.ViewOrder import ViewOrder
from ordershub.views.ViewProducts import ViewProducts
from ordershub.views.ViewShop import ViewShop

base_api_path = 'api/v1/'

router = DefaultRouter()

router.register('user/auth', UserAuth)
router.register('user/register', RegisterAccount, basename='user-register')
router.register('user/register/confirm', ConfirmAccount, basename='user-register-confirm')
router.register('user/details', AccountDetails, basename='user-details')
router.register('user/contact', ContactView, basename='user-contact')
router.register('user/login', LoginAccount, basename='user-login')
# router.register('user/password_reset', reset_password_request_token, basename='password-reset') # in path
# router.register('user/password_reset/confirm', reset_password_confirm, basename='password-reset-confirm')

router.register('shops', ViewShop, basename='shops')
router.register('category', ViewCategory, basename='category')
router.register('products', ViewProducts, basename='products')
router.register('basket', ViewBasket, basename='basket')
router.register('order', ViewOrder, basename='order')

router.register('partner/update', PartnerUpdate, basename='partner-update')
router.register('partner/state', PartnerState, basename='partner-state')
router.register('partner/orders', PartnerOrders, basename='partner-orders')

urlpatterns = [
    path(base_api_path, include(router.urls)),
    path("admin", admin.site.urls),
    path(base_api_path + 'api-token-auth', views.obtain_auth_token),  # не работает почему?
    path(base_api_path + 'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(base_api_path + 'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(base_api_path + 'token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
]
