from django.views.generic import RedirectView
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import models
from . import serializers
from .helpers import search_nutritionix


class NutritionDataListView(generics.ListAPIView):
    """API view listing nutrition data."""

    queryset = models.NutritionData.objects.all()
    serializer_class = serializers.NutritionDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['item_name']

    @staticmethod
    def create_from_nutritionix_search_result(keyword):
        """Create objects using search results from Nutritionix."""
        results = search_nutritionix(keyword)

        for res in results:
            if models.NutritionData.objects.filter(
                item_id=res['item_id']
            ).count() > 0:
                continue

            obj = models.NutritionData(
                item_id=res['item_id'],
                item_name=res['item_name'],
                calories=res['nf_calories'],
                total_fat=res['nf_total_fat'],
                total_carbohydrate=res['nf_total_carbohydrate'],
                dietary_fiber=res['nf_dietary_fiber'],
                sugars=res['nf_sugars'],
                protein=res['nf_protein'],
                serving_size_qty=res['nf_serving_size_qty'],
                serving_size_unit=res['nf_serving_size_unit'],
                serving_weight_grams=res['nf_serving_weight_grams'],
            )
            obj.save()

        return len(results)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if 'search' in request.GET.keys() and queryset.count() == 0:
            keyword = request.GET.get('search', '')
            if self.create_from_nutritionix_search_result(keyword):
                queryset = self.filter_queryset(self.get_queryset())

        limit = request.GET.get('limit', queryset.count())
        queryset = list(queryset)[:int(limit)]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NutritionDataSearchResultsView(RedirectView):
    """Redirect searches to the search-filtered list view."""

    pattern_name = 'api:nutritiondata-list'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        url = reverse(self.pattern_name)
        url = '{}?search={}'.format(url, kwargs.get('search_term', ''))
        args = self.request.META.get('QUERY_STRING', '')
        if args and self.query_string:
            url = '{}&{}'.format(url, args)
        return url
