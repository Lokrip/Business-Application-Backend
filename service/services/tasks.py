import time
import datetime

from django.db.models import (
    F
)

from django.core.cache import cache
from django.db import transaction
from django.conf import settings

from celery_singleton import Singleton
from celery import shared_task


@shared_task(base=Singleton) 
def set_price(subscription_id):
    from services.models import Subsription 

    with transaction.atomic(): 
        subscription = Subsription.objects.select_for_update().filter(id=subscription_id).annotate(
            annotated_price=F('service__full_price') - F('service__full_price') * (
                  F('plan__discount_percent') / 100.00)).first() 
        
        subscription.price = subscription.annotated_price
        subscription.save()
    cache.delete(settings.PRICE_CACHE_NAME)


@shared_task(base=Singleton) 
def set_comment(subscription_id):
    from services.models import Subsription 
    print('comment start')
    with transaction.atomic():
        subscription = Subsription.objects.select_for_update().get(id=subscription_id) 
        subscription.comment = str(datetime.datetime.now())

        subscription.save()
    cache.delete(settings.PRICE_CACHE_NAME)
    print('comment end')

    

