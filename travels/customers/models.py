from django.db import models

class Customer(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    name = models.CharField(max_length=50)
    address = models.TextField()
    mobile_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    # Metadata
    class Meta: 
        ordering = ['id']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('customer_details', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name