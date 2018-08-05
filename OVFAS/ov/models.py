from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.core.validators import RegexValidator
import os
from django.contrib.auth.models import Permission,User

class HostelBlock(models.Model):
    block_name=models.CharField(max_length=100)

    def __str__(self):
        return(self.block_name)

class OutingForm(models.Model):
    visibility=models.BooleanField(default=False)
    registration_no=models.CharField(max_length=9)
    name=models.CharField(max_length=100)
    mess_type=models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number should be up to 10 digits only")
    student_phone_number=models.CharField(validators=[phone_regex],max_length=13,default='')
    parent_phone_number=models.CharField(validators=[phone_regex],max_length=13,default='')
    hostel_block=models.ForeignKey(HostelBlock,on_delete=models.SET_NULL,null=True)
    time_of_leaving=models.TimeField(blank=False)
    time_of_arrival=models.TimeField(blank=False)
    viiting_address=models.TextField()
    purpose_of_leaving=models.CharField(max_length=250)
    permanent_address=models.TextField()
    def __str__(self):
        return(self.registration_no)



