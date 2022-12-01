from django.db import models

# Create your models here.
"""
 {
      "name": "accounts/114963299403833404828",
      "accountName": "test",
      "type": "LOCATION_GROUP",
      "role": "PRIMARY_OWNER",
      "verificationState": "UNVERIFIED",
      "vettedState": "NOT_VETTED",
      "permissionLevel": "OWNER_LEVEL"
    }
"""
class Accounts(models.Model):
    name = models.CharField(max_length=100)
    accountName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    permissionLevel = models.CharField(max_length=100)
    verificationState = models.CharField(max_length=100)
    vettedState = models.CharField(max_length=100)



