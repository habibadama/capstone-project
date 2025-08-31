from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()
 

    def __str__(self):
        return f"Reservation for {self.name} on {self.bookingDate} for {self.no_of_guests} guests"
    

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} - ${self.price} (Inventory: {self.inventory})"