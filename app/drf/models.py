from django.db import models

# Create your models here.

class Account(models.Model):
    product_options = (
        ("credit","CREDIT"),
        ("debit","DEBIT"),
        ("savings","SAVINGS"),
        ("checking","CHECKING"),
    )
    product_username = models.CharField(max_length=30)
    
    product_email = models.EmailField(max_length=30)
    
    product_options = models.CharField(
        max_length=30,
        choices = product_options,
        default = product_options[0])