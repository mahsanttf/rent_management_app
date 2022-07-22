from django.db import models


class VehicleProvider(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    v_provider = models.ForeignKey(VehicleProvider, on_delete=models.CASCADE, related_name='vehicles')
    name = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=25, unique=True)
    model_number = models.CharField(max_length=25)
    capacity = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    monthly_rent = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name + ' ' + self.vehicle_number)


class Passenger(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),  # ('Actual Value', 'Human Readable Name')
        ('Female', 'Female'),
        ('other', 'other')
    )

    ONE_SIDE = 'One-Side'
    BOTH_SIDE = 'Both-Side'

    DIRECTION_CHOICES = (
        (ONE_SIDE, 'One-Side'),  # ('Actual Value', 'Human Readable Name')
        (BOTH_SIDE, 'Both-Side')
    )

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='passengers')
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    joining_date = models.DateField(auto_now_add=True)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    fix_rent = models.PositiveIntegerField(default=0)  # Value given when needed.

    def __str__(self):
        return self.name
