import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_ref_generator(instance):
    order_new_ref= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(order_id= order_new_ref).exists()
    if qs_exists:
        return unique_order_ref_generator(instance)
    return order_new_ref