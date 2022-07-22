from django.contrib import admin
from .models import Expense, ExpenseDetails

admin.site.register(Expense)
admin.site.register(ExpenseDetails)
