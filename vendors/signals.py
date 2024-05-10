
from django.db.models.signals import post_save
from django.dispatch import receiver
from purchase_order.models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'completed':
        instance.vendor.update_performance_metrics()
