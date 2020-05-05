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
    openreading = models.IntegerField()
    closedate = models.DateField()
    closereading = models.IntegerField()

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

    @property
    def duration(self):
        return self.closedate - self.opendate

    def running(self):
        return self.closereading - self.openreading
    

class Booking_Extended(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True)
    amount_receivable = models.IntegerField()
    amount_received = models.IntegerField()
    booking_expenses = models.IntegerField()
    receivable_breakdown = models.TextField()

    @property
    def amount_pending(self):
        return self.amount_receivable - self.amount_received

    def our_income(self):
        return self.amount_receivable - self.booking_expenses
