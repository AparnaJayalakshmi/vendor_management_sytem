from django.db import models
from django.utils import timezone
from vendors.models import Vendor

# Create your models here.

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100,unique=True,blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True, db_constraint=False)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField(null=True,blank=True)
    acknowledgement_date = models.DateTimeField(null=True,blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):    
        if not self.pk:
            # Newly created object, so set the creation date
            self.order_date = timezone.now()
            self.issue_date = self.order_date

        super().save(*args, **kwargs)

    
   
    