from rest_framework import serializers
from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    camera = serializers.StringRelatedField()
    screen_resolution = serializers.StringRelatedField()
    color = serializers.StringRelatedField()
    so = serializers.StringRelatedField()

    class Meta:
        model = Phone
        fields = '__all__'
