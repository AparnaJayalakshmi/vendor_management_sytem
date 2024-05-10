from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer

class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate
        }
        return Response(data)
    
    @action(detail=True, methods=['get'])
    def historical_performance(self, request, pk=None):
        vendor = self.get_object()
        historical_performances = HistoricalPerformance.objects.filter(vendor=vendor)
        serializer = HistoricalPerformanceSerializer(historical_performances, many=True)
        return Response(serializer.data)


    
