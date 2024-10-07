from rest_framework import serializers

from src.cats.models.cats import CatsModel

class CatsSerializer(serializers.ModelSerializer):
    '''Serializer for Cats model.'''
    
    class Meta:
        model = CatsModel
        field = ('__all__',)


class CreateCatsSerializer(serializers.ModelSerializer):
    '''Serializer for create cats model.'''
    
    class Meta:
        model = CatsModel
        field = ('__all__',)

    def create(self, validated_data):
        return CatsModel.objects.create(**validated_data)