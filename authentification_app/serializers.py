from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'first_name', 'last_name', 'birth_date', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UtilisateurSerializer, self).create(validated_data)


class UtilisateurUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
