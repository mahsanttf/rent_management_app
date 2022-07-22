from django.db import models
from vehicles.models import Vehicle, Passenger


class Expense(models.Model):
    MONTH_CHOICES = (
        ('January', 'January'),  # ('Actual Value', 'Human Readable Name')
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='expenses')
    exp_month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    rent = models.PositiveIntegerField(blank=True)  # Monthly rent of vehicle.
    final_rent = models.PositiveIntegerField()  # After adding or subtracting local passengers.


class ExpenseDetails(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='expense_details')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='passenger_expense')
    total_rent = models.PositiveIntegerField()  # Expense/rent of a single passenger.

    def __str__(self):
        return self.passenger.name
