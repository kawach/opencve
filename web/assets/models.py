from django.db import models

from opencve.models import BaseModel
from organizations.models import Organization
from cves.models import Product

class Asset(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    class Meta:
        db_table = "opencve_assets"

    def __str__(self):
        return self.name
