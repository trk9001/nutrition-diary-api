from django.contrib import admin

from . import models

admin.site.site_header = 'Nutrition Diary API Administration'
admin.site.site_title = 'Nutrition Diary API'
admin.site.index_title = 'Admin'

admin.site.register(models.NutritionData)
