from django.db import models

# Create your models here.

class Pay(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13, null=True)
    credit_No = models.CharField(max_length=9, null=True)
    crPass=models.CharField(max_length=10)
    timeCreated=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cash=models.IntegerField(blank=False, null=True, default=0, auto_created=True)
    def __str__(self) -> str:
        return self.name
    


class Transfers(models.Model):
    cho= (        
        ('done','done'),
        ('Erorr','Erorr'))   
    
    frome  = models.CharField(max_length=9)
    to  = models.CharField(max_length=9)
    time  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=10, choices=cho )
    amount = models.CharField(max_length=6)
    def __str__(self) -> str:
        return self.frome