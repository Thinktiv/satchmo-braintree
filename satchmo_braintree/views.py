from django.views.decorators.cache import never_cache
from django.conf import settings

from livesettings import config_get_group
from payment.views import confirm, payship
from satchmo_braintree import *

def pay_ship_info(request):
    if hasattr(settings, 'CREDIT_PAY_SHIP_INFO'):
        custom_allow_func = import_func_from_string(settings.CREDIT_PAY_SHIP_INFO)
        return custom_allow_func(request, config_get_group('PAYMENT_SATCHMO_BRAINTREE'))
    else:
        return payship.credit_pay_ship_info(request, config_get_group('PAYMENT_SATCHMO_BRAINTREE'))
pay_ship_info = never_cache(pay_ship_info)
    
def confirm_info(request):
    return confirm.credit_confirm_info(request, config_get_group('PAYMENT_SATCHMO_BRAINTREE'))
confirm_info = never_cache(confirm_info)
