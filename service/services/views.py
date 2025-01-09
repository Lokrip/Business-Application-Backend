from django.db.models import (
    Prefetch,
    Sum,
)
from django.core.cache import cache
from django.shortcuts import render
from django.conf import settings

from rest_framework.viewsets import ReadOnlyModelViewSet


from .models import Subsription, Client
from .serializers import SubsriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subsription.objects.order_by('-pk').prefetch_related(
        "plan",
        Prefetch('client', queryset=Client.objects.all().select_related('user').only(
            'company_name', 'user__email'
        ))
    )

    serializer_class = SubsriptionSerializer 
    
    def list(self, request, *args, **kwargs): 
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        price_cache = cache.get(settings.PRICE_CACHE_NAME)
        
        if price_cache: 
            total_price = price_cache
        else:
            total_price = queryset.aggregate(total=Sum('price')).get('total') 
            cache.set(settings.PRICE_CACHE_NAME, total_price, 60 * 60)

        response_data = {'result': response.data}
        response_data['total_amount'] = total_price
        response.data = response_data
        
        return response
