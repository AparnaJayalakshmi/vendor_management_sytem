from django.db import models
from django.db.models import Count, F, Sum
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def update_performance_metrics(self):
        completed_orders = self.purchaseorder_set.filter(status='completed')
        total_orders = self.purchaseorder_set.all()

        # On-Time Delivery Rate
        on_time_delivery_count = completed_orders.filter(delivery_date__lte=F('promised_delivery_date')).count()
        on_time_delivery_rate = (on_time_delivery_count / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0

        # Quality Rating Average
        quality_rating_sum = completed_orders.aggregate(Sum('quality_rating'))['quality_rating__sum'] or 0
        quality_rating_avg = quality_rating_sum / completed_orders.count() if completed_orders.count() > 0 else 0

        # Average Response Time
        response_time_sum = sum([(order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders])
        average_response_time = response_time_sum / completed_orders.count() if completed_orders.count() > 0 else 0

        # Fulfilment Rate
        fulfilled_orders_count = completed_orders.filter(issues__isnull=True).count()
        fulfillment_rate = (fulfilled_orders_count / total_orders.count()) * 100 if total_orders.count() > 0 else 0

        # Update historical performance
        HistoricalPerformance.objects.create(
            vendor=self,
            date=timezone.now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

    
    def __str__(self):
        return self.name

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()