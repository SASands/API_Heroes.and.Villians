from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType
from . import serializers




@api_view(['GET'])
def super_types_list(request):
    super_types = SuperType.objects.all()

    serializer = SuperTypeSerializer(super_types, many=True)



    return Response(serializer.data)

    

