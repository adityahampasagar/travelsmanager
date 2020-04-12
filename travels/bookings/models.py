from django.db import models
from customers.models import Customer
from vehicles.models import Vehicle
from drivers.models import Driver

class Booking(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    place = models.CharField(max_length=25)
    opendate = models.DateField()
    openreading = models.CharField(max_length=8)
    closedate = models.DateField()
    closereading = models.CharField(max_length=8)

    # Metadata
    class Meta: 
        ordering = ['id']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('booking_details', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.id)