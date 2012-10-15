from django.views.decorators.cache import never_cache
from django.conf import settings as django_settings

from livesettings import config_get_group

from satchmo_braintree import import_func_from_string

def pay_ship_info(request):
    credit_pay_ship_info = import_func_from_string(getattr(django_settings, 'CREDIT_PAY_SHIP_INFO', 'payment.views.payship.credit_pay_ship_info'))
    return credit_pay_ship_info(request, config_get_group('PAYMENT_SATCHMO_BRAINTREE'))
pay_ship_info = never_cache(pay_ship_info)

def confirm_info(request):
    credit_confirm_info = import_func_from_string(getattr(django_settings, 'CREDIT_CONFIRM_INFO', 'payment.views.confirm.credit_confirm_info'))
    return credit_confirm_info(request, config_get_group('PAYMENT_SATCHMO_BRAINTREE'))
confirm_info = never_cache(confirm_info)
