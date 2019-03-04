from django.db import models
from django.core.exceptions import ValidationError


class seller(models.Model):
    def rating_check(self, rating):
        if self.rating < 1 and self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5')

    username = models.CharField(max_length=50)

    password = models.CharField(max_length=50)

    thumbnail = models.ImageField(
        height_field=1000, width_field=1000, max_length=(1000 * 1000 * 3 + 100000)
    )

    rating = models.FloatField(
        db_index=True, validators=[rating_check]
    )


class product(models.Model):
    def price_check(self, price):
        if self.price < 0:
            raise ValidationError('Price must be a positive value')

    def rating_check(self, rating):
        if self.rating < 1 and self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5')

    id = models.BigIntegerField(
        primary_key=True, unique=True, editable=False, db_index=True, auto_created=True
    )

    thumbnail = models.ImageField(
        height_field=1000, width_field=1000, max_length=(1000 * 1000 * 3 + 100000)
    )

    title = models.CharField(max_length=127)

    description = models.CharField(max_length=1023)

    price = models.FloatField(db_index=True, validators=[price_check])

    valuta = models.CharField(
        max_length=3, choices=(
            ('Dollars', 'USD'),
            ('Euro', 'EUR'),
            ('Bitcoin', 'BTC')
        )
    )

    rating = models.FloatField(
        db_index=True, validators=[rating_check], null=True
    )

    venditore = models.ForeignKey(to=seller, on_delete=models.CASCADE)
