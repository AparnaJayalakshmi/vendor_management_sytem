from django.urls import path,include
from rest_framework.routers import DefaultRouter
from vendors.views import VendorModelViewSet
from purchase_order.views import PurchaseOrderViewSet

router = DefaultRouter()
router.register('vendors', VendorModelViewSet, basename='vendor')
router.register('purchase_orders', PurchaseOrderViewSet, basename='purchase_order')


urlpatterns = [
    # Include the URLs generated by the router
    path('',include(router.urls)),


]