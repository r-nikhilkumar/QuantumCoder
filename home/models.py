from django.db import models

# Create your models here.
class user_contact_details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.BigIntegerField()
    comment = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.name
