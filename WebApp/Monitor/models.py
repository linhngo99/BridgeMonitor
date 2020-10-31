from django.db import models

# Create your models here.

class SensorNode(models.Model):
    """Model representing a sensor node."""

    name = models.CharField(max_length=200, help_text='Name the sensor Node')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    STATUS = (
        ('On'),
        ('Off'),
    )


class Sensor(models.Model):
    """Model representing a Sensor."""

    name = models.CharField(max_length=200, help_text='Name the sensor type')

    # Foreign Key used because a sensor belong to one sensor node, but sensor nodes have multiple sensors
    SensorNode = models.ForeignKey(SensorNode, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
