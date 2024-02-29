from django.db import models

class LandingPagePermission(models.Model):
    class Meta:
        permissions = [
            ("can_access_own_products", "Can Access Own Products"),
        ]
