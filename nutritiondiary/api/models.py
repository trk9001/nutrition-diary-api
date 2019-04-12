from django.db import models


def get_upload_path(instance, filename):
    """Customized upload path for every object."""
    return 'uploads/{}/{}'.format(instance.id, filename)


class NutritionData(models.Model):
    """Model representing nutrition information for a particular food."""

    item_id = models.CharField(
        max_length=25,
        help_text='(Item ID as obtained from the Nutritionix API)',
        blank=True,
    )
    item_name = models.CharField(
        max_length=500,
    )
    item_image = models.ImageField(
        max_length=200,
        upload_to=get_upload_path,
        blank=True,
        null=True,
    )
    calories = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    total_fat = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    total_carbohydrate = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    dietary_fiber = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    sugars = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    protein = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    serving_size_qty = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
    serving_size_unit = models.CharField(
        max_length=300,
        blank=True,
    )
    serving_weight_grams = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
    )
