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
router.register('products', ViewProducts, basename="products")
router.register('shops', ViewShop, basename="shops")
router.register('categories', ViewCategory, basename="categories")

urlpatterns = [
    path("admin", admin.site.urls),
    path(base_api_path, include(router.urls)),
    path(base_api_path + 'api-token-auth', views.obtain_auth_token),  # не работает почему?
    path(base_api_path + 'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(base_api_path + 'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(base_api_path + 'token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path(base_api_path + 'partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path(base_api_path + 'partner/state', PartnerState.as_view(), name='partner-state'),
    path(base_api_path + 'partner/orders', PartnerOrders.as_view(), name='partner-orders'),

    path(base_api_path + 'user/register', RegisterAccount.as_view(), name='user-register'),
    path(base_api_path + 'user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path(base_api_path + 'user/login', LoginAccount.as_view(), name='user-login'),
    path(base_api_path + 'user/auth', UserAuth.as_view(), name='user-auth'),
    path(base_api_path + 'user/details', AccountDetails.as_view(), name='user-details'),
    path(base_api_path + 'user/contact', ContactView.as_view(), name='user-contact'),
    path(base_api_path + 'user/password_reset', reset_password_request_token, name='password-reset'),
    path(base_api_path + 'user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),

    # path(base_api_path + 'categories', ViewCategory.as_view(), name='categories'),
    # path(base_api_path + 'shops', ViewShop.as_view(), name='shops'),
    # path(base_api_path + 'products', ViewProducts.as_view(), name='products'),
    path(base_api_path + 'basket', ViewBasket.as_view(), name='basket'),
    path(base_api_path + 'order', ViewOrder.as_view(), name='order'),
]
