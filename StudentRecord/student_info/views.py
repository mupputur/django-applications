from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentInfoModel
from .serializers import StudentInfoModelSerializers
from rest_framework.parsers import JSONParser
# Create your views here.


# API developemnet


@api_view(["GET", "POST"])
def student(request):
    if request.method == "GET":
        # all data from data base
        student_data_all = StudentInfoModel.objects.all()
        # serializer data
        serializer = StudentInfoModelSerializers(student_data_all, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentInfoModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()  # saves the data in db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", 'DELETE'])
def details(request, pk):
    try:
        student_data_all = StudentInfoModel.objects.get(pk=pk)
    except StudentInfoModel.DoesNotExist:
        return Response({'message': 'The student_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentInfoModelSerializers(student_data_all)
        return Response(serializer.data)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        serializer = StudentInfoModelSerializers(student_data_all, data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student_data_all.delete()
        return Response(status=204)

"""
def get_student():
    pass

def set_student():
    pass
"""