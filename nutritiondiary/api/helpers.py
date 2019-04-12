import decimal

import requests
from django.conf import settings


def search_nutritionix(keyword):
    """Search for the keyword using the Nutritionix API."""

    max_results = 20
    search_fields = [
        'item_id', 'item_name', 'nf_calories', 'nf_sugars', 'nf_protein',
        'nf_total_fat', 'nf_total_carbohydrate', 'nf_dietary_fiber',
        'nf_serving_weight_grams', 'nf_serving_size_qty',
        'nf_serving_size_unit'
    ]
    search_url = 'https://api.nutritionix.com/v1_1/search/{}'.format(keyword)
    payload = {
        'results': '0:{}'.format(max_results),
        'fields': ','.join(search_fields),
        'appId': settings.NUTRITIONIX_APP_ID,
        'appKey': settings.NUTRITIONIX_APP_KEY,
    }

    r = requests.get(search_url, params=payload)
    resp = r.json(parse_float=decimal.Decimal, parse_int=decimal.Decimal)
    results = []
    if resp['total_hits'] > 0:
        for hit in resp['hits']:
            results.append(hit['fields'])

    return results
