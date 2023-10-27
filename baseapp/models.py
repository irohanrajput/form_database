from django.db import models

class Details(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False )  
    user_feedback = models.CharField(max_length=200, null=False, blank=False)
    contact_via_phone = models.CharField(max_length=200, null=False, blank=False, default=False)
    contact_via_email = models.CharField(max_length=200, null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Name}'