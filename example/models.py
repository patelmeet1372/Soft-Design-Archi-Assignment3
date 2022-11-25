from django.db import models


class ProdInvt(models.Model):
    item_bc = models.CharField(max_length=100)
    item_details = models.CharField(max_length=100)




