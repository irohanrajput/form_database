from django.db import models

class Details(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False )  
    What_Users_Say = models.CharField(max_length=200, null=False, blank=False)
    if_selected = models.CharField(max_length=200, null=False, blank=False)
    # if_selected = models.BooleanField()
    def __str__(self):
        return self.title