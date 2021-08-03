from django.db import models

# Create your models here.


class Survey(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100,null=True)
    email_id = models.EmailField(null=True)
    contact_no = models.IntegerField(null=True)
    zip_code = models.IntegerField(null=True)
    city = models.CharField(max_length=100,null=True)
    own_house = models.BooleanField(null=True)
    fully_vaccinated = models.BooleanField(null=True)
    profile_icon = models.ImageField(upload_to="images",null=True)
    vaccine_proof = models.FileField(upload_to="files",null=True)
    