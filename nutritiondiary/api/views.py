from rest_framework import filters, generics, views

from . import models
from . import serializers


class NutritionDataView(generics.ListAPIView):
    """API view listing nutrition data."""

    queryset = models.NutritionData.objects.all()
    serializer_class = serializers.NutritionDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['item_name']
