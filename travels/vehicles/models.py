from django.db import models

class Vehicle(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    registration = models.CharField(max_length=10)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=50)
    registration_date = models.DateField()
    insurance_expiry = models.DateField()
    road_tax_expiry = models.DateField()
    fitness_expiry = models.DateField()
    authorization_expiry = models.DateField()
    permit_expiry = models.DateField()
    emission_expiry = models.DateField()

    # Metadata
    class Meta: 
        ordering = ['id']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('vehicle_details', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.registration