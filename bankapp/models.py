from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=200,blank=True,unique = True)
    def __str__(self):
        return self.city_name
class Bank(models.Model):
    bank_name = models.CharField(max_length = 300,blank=True,unique=True)
    headquarter = models.ForeignKey(City,related_name="headquartes",to_field="city_name",on_delete=models.CASCADE,default="")
    address = models.CharField(max_length=200,blank=True)
    contact = models.IntegerField()
    def __str__(self):
        return self.bank_name

class Branch(models.Model):
    bank = models.ForeignKey(Bank,related_name="branch",to_field="bank_name",on_delete=models.CASCADE)
    city =  models.ForeignKey(City,related_name="city",to_field="city_name",on_delete=models.CASCADE,default="")
    location = models.CharField(max_length=200,blank=True,null=True)
    ifsc_code = models.CharField(max_length=12,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return str(self.bank) + " Branch: "+str(self.city) + " IFSC: "+ (self.ifsc_code)



