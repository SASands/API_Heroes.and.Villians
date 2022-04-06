from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .serializers import SuperTypeSerializer
from .models import SuperType
from . import serializers
import super_types
import supers








@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        super_types = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
    product = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializers = SuperTypeSerializer(super_types)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializers = SuperTypeSerializer(super_types, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save
        return Response(serializers.data)
    elif request.method == 'DELETE':
        SuperType.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

