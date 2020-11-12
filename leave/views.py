from django.shortcuts import render
from .serializers import leaveSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import leaveSerializer,approve_leaveSerializer
from .models import leave

# Create your views here.

@api_view(['POST'])
def apply_leave(request):
    serializer = leaveSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def all_leave_applications(request):
    leaves =  leave.objects.all()
    serializer = leaveSerializer(leaves, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def single_leave_application(request, id):
    leave_application = leave.objects.get(id = id)
    serializer = leaveSerializer(leave_application, many = False)

    return Response(serializer.data)

@api_view(['POST'])
def approve_leave(request, id):
    leaves = leave.objects.get(id = id)
    serializer = approve_leaveSerializer(instance = leaves, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)