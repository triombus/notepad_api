from rest_framework import viewsets

from purchase.models import Purchase, PurchaseItem
from purchase.serializers import PurchaseSerializer, PurchaseItemSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer
