from django.db import models
from django.utils import timezone

# Create your models here.
class Inventory(models.Model):
    donor_name = models.CharField(max_length = 100, null=False, blank = False)
    item_type = models.CharField(max_length = 100, null=False, blank = False)
    amount = models.DecimalField(max_digits = 19, decimal_places = 2, null=False, blank = False)
    location = models.CharField(max_length = 100, null=False, blank = False)
    date = models.DateField(default=timezone.now)
    

    def __str__(self) -> str:
        return self.donor_name + ' hello'
