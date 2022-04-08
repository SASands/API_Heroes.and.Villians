from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .serializers import SupersSerializer
from .models import Supers
from . import serializers
import super_types 
import supers


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        queryset = Supers.objects.all()
        serializer = SupersSerializer(queryset, many=True)
        villains = queryset.filter(super_type__type= 'Villain')
        heroes = queryset.filter(super_type__type= 'Hero')
        heroes_serialized = SupersSerializer(heroes, many=True)
        villains_serialized = SupersSerializer(villains, many=True)
        if request.query_params.get('type') == 'hero':
            # custom_response = heroes_serialized.data
            return Response(heroes_serialized.data, status=status.HTTP_200_OK)    
        elif request.query_params.get('type') == 'villain':
            # custom_response = villains_serialized.data
            return Response(villains_serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
 



@api_view(['GET', 'PUT','DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializers = SupersSerializer(supers)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = SupersSerializer(supers, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save
        return Response(serializers.data) 
    elif request.method == 'DELETE':
        supers.delete
        return Response(status=status.HTTP_404_NOT_FOUND)



        
# @api_view(['GET'])
# def supers_detail(request):
#     if request.method == 'Get_All_Heroes':
#         queryset = Supers.objects.all(heroes)
#         heroes = queryset.filter(super_types__1 = 'Hero')
#         serializers = SupersSerializer(supers, data=request.data)
#         return Response(serializers.data)
#     elif request.method == 'Get_All_Villains':
#         queryset = Supers.objects.all(villains)
#         villains = queryset.filter(super_types__2 = 'Villain')
#         serializers = SupersSerializer(supers, data=request.data)
#         return Response(serializers.data)




# @api_view(['Get'])
# def supers_list(request):
#     super_types_param = request.query_params.get('super_types')
#     sort_param = request.query_params.get('sort')
#     supers = Supers.objects.all()
#     if super_types_param:
#         supers = supers.filter(super_types=super_types_param)
#     elif sort_param:
#         supers = supers.order_by(sort_param)
#         serializers = SupersSerializer(supers, many=True)
#         return Response(serializers.data)


@api_view(['Get'])
def super_types_list(request):
    appending_dict_example = {}
    appending_dict_example['']








    