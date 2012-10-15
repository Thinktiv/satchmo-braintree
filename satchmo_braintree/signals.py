from django.dispatch import Signal

satcho_braintree_order_validate = Signal(providing_args = ['data','order'])
