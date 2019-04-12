from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'api'

patterns_v1 = [
    path(
        'list/',
        views.NutritionDataListView.as_view(),
        name='nutritiondata-list',
    ),
    path(
        'search/<search_term>/',
        views.NutritionDataSearchResultsView.as_view(),
        name='nutritiondata-searchresults',
    ),
]

urlpatterns = [
    path('v1/', include(patterns_v1)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
