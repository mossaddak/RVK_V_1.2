from django.db import models
from accounts.models import(
    User
)




# Create your models here.
class DonationModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name="Donation")

    first_name = models.CharField(max_length=250,null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=250, null=True, verbose_name="Last Name")
    email = models.CharField(max_length=250, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=250, null=True, verbose_name="Phone Number")
    address = models.TextField(null=True, verbose_name="Address")

    do_you_benifited = models.BooleanField(null=True)
    
    pin_code = models.CharField(null=True, max_length=250, verbose_name="Pin Code")
    city = models.CharField(null=True, max_length=250, verbose_name="City")
    state = models.CharField(max_length=250, null=True, verbose_name="State")
    country = models.CharField(max_length=250, null=True, verbose_name="Country")

    pan = models.CharField(max_length=250, null=True, verbose_name="PAN")


    amount = models.CharField(max_length=50, null=True)
    payment_id = models.CharField(max_length=100, null=True)
    isPaid = models.BooleanField(default=False, null=True)
    order_date = models.DateTimeField(auto_now=True, null=True)

    document = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}.{self.payment_id}"