from rest_framework import serializers
from .models import Supers

class Supers(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primairy_ability', 'secondary_ability', 'catchphrase', 'super_type']
        