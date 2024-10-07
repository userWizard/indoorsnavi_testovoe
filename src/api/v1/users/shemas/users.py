from rest_framework import serializers

from src.users.models.users import UserModel


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for users'''

    class Meta:
        model = UserModel
        fields = ('__all__')


class UserCreateSerializer(serializers.ModelSerializer):
    '''Serializer for create users'''

    class Meta:
        model = UserModel
        fields = ('__all__')

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)
