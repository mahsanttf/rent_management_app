from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('expense/', views.ExpenseCreate.as_view(), name='expense_create'),
]
