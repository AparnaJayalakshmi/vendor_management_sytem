from rest_framework import serializers
from .models import Vendor
from .models import HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
    vendor_code = serializers.CharField(read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'

    def create(self, validated_data):
        existing_vendors_count = Vendor.objects.count()
        vendor_code = f'V{existing_vendors_count + 1:03}'
        validated_data.pop('vendor_code', None)  # Remove vendor_code from validated_data
        validated_data['vendor_code'] = vendor_code
        return super().create(validated_data)
    
class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
