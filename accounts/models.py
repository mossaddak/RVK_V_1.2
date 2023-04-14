from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
import uuid


#user model for application
class User(AbstractUser):
    # value to determine if user is verified
    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=5, null=True, blank=True)

    # unique phone number
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)

    email = models.EmailField(unique=True)

    smart_card = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    
    country = models.CharField(max_length=255, blank=True, default="None")

    dob = models.DateTimeField(blank=True, null=True)

    gender = models.CharField(max_length=25, blank=True, null=True)

    age = models.IntegerField(blank=True, null=True)
 
    profile_picture = models.ImageField( blank=True, null=True)




    #remove username
    username = None
    first_name = None
    last_name = None

    objects = CustomUserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"


    def __str__(self):
        return f"{self.pk}.{self.email}"

    # allow phone number to be blank but unique
    def clean(self):
        if self.phone_number is not None and len(self.phone_number.strip()) == 0:
            self.phone_number = None




class UserVerification(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    used = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.token)
    
