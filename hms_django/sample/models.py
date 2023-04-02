from Services.models import Service
import os
from django.db import models
import datetime
from datetime import date,datetime
from datetime import timedelta
from django.db.models import Sum

class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    specialization_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name


class Invoice(models.Model):

    CLIENT_ID_DEFAULT = None

    invoice_id = models.AutoField(primary_key=True)
    date_created=models.DateField()
    invoice_status = models.CharField(max_length=255)
    invoice_description=models.CharField(max_length=255, null=True)
    invoice_amount=models.IntegerField()
    invoice_client = models.ForeignKey(Client, on_delete=models.CASCADE,default=CLIENT_ID_DEFAULT,null=True)

    def invoice_get_amount(self):
        return none

    def __str__(self):
        return self.invoice_client.client_name + " | " 

class Invoice_Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    entry_service = models.ForeignKey(Service,on_delete=models.CASCADE)
    entry_invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    entry_qty = models.IntegerField()
    entry_rate = models.IntegerField()
    def __str__(self):
        return self.entry_service.service_name #

class Receiving(models.Model):
    receiving_id=models.AutoField(primary_key=True)
    date_created = models.DateField()
    receiving_amount = models.IntegerField()
    receiving_description=models.CharField(max_length=255,null=True)
    receiving_client = models.ForeignKey(Client,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.receiving_client.client_name + " | " + str(self.receiving_amount)