from django.db import transaction
from django.forms import forms
from django.shortcuts import render
from django.views import generic
from .models import Expense
from vehicles.models import Vehicle


class ExpenseCreate(generic.CreateView):
    model = Expense
    fields = [
        'vehicle', 'exp_month',
    ]
    #
    # def form_valid(self, form):
    #     vehicles = self.object.
    #     self.object.rent = vehicles.monthly_rent
    #     self.object.final_rent = self.object.rent
    #     self.object.save()
