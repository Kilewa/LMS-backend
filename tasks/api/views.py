from django.shortcuts import render
from .models import task
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskSerializer, task_statusSerializer


# Create your views here.

@api_view(['GET'])
def all_tasks(request):
    tasks = task.objects.all()
    serializer = taskSerializer(tasks, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def single_task(request, id):
    tasks = task.objects.get(id = id)
    serializer = taskSerializer(tasks, many = False)

    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = taskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update_task_status(request, id):
    tasks = task.objects.get(id = id)
    serializer = task_statusSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, id):
    tasks = task.objects.get(id = id)
    tasks.delete()

    return Response('Task successfully deleted')













