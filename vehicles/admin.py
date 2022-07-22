from django.contrib import admin
from .models import Passenger, VehicleProvider, Vehicle

admin.site.register(Passenger)
admin.site.register(VehicleProvider)
admin.site.register(Vehicle)
