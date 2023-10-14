from django.db import models

class addDetails(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    phone = models.IntegerField(("Phone number"))
    yviews = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.title