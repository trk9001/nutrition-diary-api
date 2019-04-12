from rest_framework import serializers

from . import models


class NutritionDataSerializer(serializers.ModelSerializer):
    """Object serializer for proper API represesntation."""

    class Meta:
        model = models.NutritionData
        fields = ['id', 'item_id', 'item_name', 'item_image', 'calories',
                  'total_fat', 'total_carbohydrate', 'dietary_fiber', 'sugars',
                  'protein', 'serving_size_qty', 'serving_size_unit',
                  'serving_weight_grams']


class NutritionDataListSerializer(serializers.Serializer):
    """Nested list serializer for use in search results."""

    total_hits = serializers.IntegerField(min_value=0)
    hits = NutritionDataSerializer(many=True, read_only=True)
