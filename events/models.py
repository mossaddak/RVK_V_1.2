from django.db import models
from django.contrib.auth import get_user_model
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import User
 
User = get_user_model()



class Event(models.Model):
    user = models.ManyToManyField(User, related_name="event_user", blank=True)

    event_name = models.CharField(max_length=255, verbose_name="Event Name", null=True)
    host_name = models.CharField(max_length=255, verbose_name="Host Name", null=True)
    
    event_image = models.ImageField(blank=True, verbose_name="Event Image", null=True)
    
    location = models.CharField(max_length=255, null=True)
    capacity = models.PositiveIntegerField(null=True)
    details = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    start = models.DateTimeField(verbose_name="Event Start Time", null=True)

    is_event_complete = models.BooleanField(verbose_name="Is event completed?", null=True, default=False)

    event_price = models.CharField(max_length=250, null=True, blank=True, verbose_name="Event Price")


    def __str__(self):
        return f"{self.pk}.{self.event_name}"
    
    class Meta:
        verbose_name_plural = 'Events'


# class FreeEvent(models.Model):
#     user = models.ManyToManyField(User, related_name="free_event_user", blank=True)

#     event_name = models.CharField(max_length=255, verbose_name="Event Name", null=True)
#     host_name = models.CharField(max_length=255, verbose_name="Host Name", null=True)
    
#     event_image = models.ImageField(blank=True, verbose_name="Event Image", null=True)
    
#     location = models.CharField(max_length=255, null=True)
#     capacity = models.PositiveIntegerField(null=True)
#     details = models.TextField(blank=True, null=True)

#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True)

#     start = models.DateTimeField(verbose_name="Event Start Time", null=True)

#     is_event_complete = models.BooleanField(verbose_name="Is event completed?", null=True, default=False)


#     def __str__(self):
#         return f"{self.pk}.{self.event_name}"
    
#     class Meta:
#         verbose_name_plural = 'Free Event'
    

class EventRegisterUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", verbose_name="User")
    first_name = models.CharField(max_length=250,null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=250, null=True, verbose_name="Last Name")
    email = models.CharField(max_length=250, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=250, null=True, verbose_name="Phone Number")
    smart_card_number = models.CharField(max_length=250, null=True, verbose_name="Smart Card Number")
    address = models.TextField(null=True, verbose_name="Address")
    pin_code = models.CharField(null=True, max_length=250, verbose_name="Pin Code")
    city = models.CharField(null=True, max_length=250, verbose_name="City")
    state = models.CharField(max_length=250, null=True, verbose_name="State")
    country = models.CharField(max_length=250, null=True, verbose_name="Country")
    #payment details
    card_details = models.CharField(max_length=20, null=True)
    amount = models.CharField(max_length=250, null=True)
    payment_id = models.CharField(max_length=100, null=True)
    order_date = models.DateTimeField(auto_now=True, null=True)
    is_pay = models.BooleanField(default=False,null=True)
    booking_id = models.CharField(max_length=7, null=True, blank=False)

    document = models.FileField(null=True, blank=True)

    #token = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.user}"
    

