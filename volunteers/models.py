from django.db import models




class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    area_of_interest = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    age = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
    
class VolunteerDescription(models.Model):
    description = models.TextField(null=True, blank=False)


    def __str__(self):
        return f"{self.pk}.{self.description}"

    class Meta:
        verbose_name_plural = 'Volunteer Description'


