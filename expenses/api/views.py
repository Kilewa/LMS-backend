from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExpensesSerializer,ApproveExpensesSerializer
from .models import expenses
from rest_framework.generics import GenericAPIView

# Create your views here.


@api_view(['POST'])
def apply_expense(request):
    serializer = ExpensesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    return Response('invalid request')

@api_view(['GET'])
def view_all_expenses(request):
    expenses =  expenses.objects.all()
    serializer = ExpensesSerializer(expenses, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def view_expense(request, id):
    expenses_app = expenses.objects.get(id = id)
    serializer = ExpensesSerializer(expenses_app, many = False)

    return Response(serializer.data)

@api_view(['POST'])
def approve_expenses(request, id):
    expenses = expenses.objects.get(id = id)
    serializer = ApproveExpensesSerializer(instance = expenses, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_expense(request,id):
    expense_app = expenses.objects.get(id = id)
    expense_app.delete()

    return Response('Successfully deleted')