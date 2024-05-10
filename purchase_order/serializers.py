from rest_framework import serializers
from django.utils import timezone
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d-%B-%Y , %I:%M%p", required=False)
    delivery_date = serializers.DateTimeField(format="%d-%B-%Y , %I:%M%p", required=False)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ['delivery_date']

    def create(self, validated_data):
        # Set order_date to the current date if not provided
        validated_data.setdefault('order_date', timezone.now())
        
        # Calculate delivery date as 7 days from the order date
        validated_data['delivery_date'] = validated_data['order_date'] + timezone.timedelta(days=7)
        
        last_po_number = PurchaseOrder.objects.all().order_by('id').last()
        if not last_po_number:
            validated_data['po_number'] = 'P001'
        else:
            po_number = 'P' + str(last_po_number.id + 1).zfill(3)
            validated_data['po_number'] = po_number

        return PurchaseOrder.objects.create(**validated_data)

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity cannot be zero or negative.")
        return value

    def validate_quality_rating(self,value):
        current_status = self.instance.status
        if current_status.lower() != 'completed':
            raise serializers.ValidationError('Cannot give Quality rating ')
        if value not in range(1,11):
            raise serializers.ValidationError('Quality Rating must between 1-10')
        
        return value
