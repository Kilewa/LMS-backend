from django.urls import path, include
from expenses.api.views import (
    apply_expense, view_all_expenses, view_expense, approve_expenses, delete_expense
)


urlpatterns = [
    path('apply_expense/',apply_leave, name='apply_expense' ),
    path('expense/applications/',view_all_expenses, name='view_all_expenses' ),
    path('single-expense/application/(\d+)/',view_expense, name='view_expense' ),
    path('approve-expense/(\d+)/',approve_expenses, name='approve_expenses'),
    path('delete-expense/(\d+)/',delete_expense, name='delete_expense')
]