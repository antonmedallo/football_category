from rest_framework import serializers
from categoryApp.models import Categories,Players

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories 
        fields=('CategoryId','CategoryName','CategoryAncestorId')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Players 
        fields=('PlayerId','PlayerName','DateOfBirth','PhotoFileName','Category')