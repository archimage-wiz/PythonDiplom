from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from ordershub.models import ConfirmEmailToken, User


# load_dotenv()
#
# CELERY_BROKER = os.getenv("CELERY_BROKER")
# CELERY_BACKEND = os.getenv("CELERY_BACKEND")
#
# celery_app = Celery("ordershub", backend=CELERY_BACKEND, broker=CELERY_BROKER)


@shared_task()
def password_reset_token(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токен для сброса пароля
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param kwargs:
    :return:
    """
    # send an e-mail to the user

    msg = EmailMultiAlternatives(
        subject=f"Password Reset Token for {reset_password_token.user}",
        body=reset_password_token.key,
        from_email=settings.EMAIL_HOST_USER,
        to=[reset_password_token.user.email]
    )
    msg.send()


@shared_task()
def new_user_registered(user_id, **kwargs):
    """
    Отправляем письмо с подтверждением почты
    """
    # send an e-mail to the user
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(subject=f"Password Reset Token for {token.user.email}",
                                 body=token.key,
                                 from_email=settings.EMAIL_HOST_USER,
                                 to=[token.user.email]
                                 )
    msg.send()


@shared_task()
def new_order(user_id, **kwargs):
    """
    Отправляем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        subject=f"Обновление статуса заказа",
        body='Заказ сформирован',
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    msg.send()
