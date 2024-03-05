from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        product = models.Product.objects.create(**validated_data)
        return product