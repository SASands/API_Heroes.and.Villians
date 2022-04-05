from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers
from . import serializers


@api_view(['GET'])
def supers_list(request):
    supers = Supers.objects.all()
    serializer = SupersSerializer(supers, many=True)
    return Response(serializer.data)





    