from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.decorators import action


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def list(self, request):
        queryset = self.get_queryset()
        vendor_id = request.query_params.get('vendor_id')
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
        serializer = PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return PurchaseOrder.objects.all()
    
    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        return Response({'message': 'Purchase Order acknowledged successfully'})