from rest_framework import serializers
from .models import Blog

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1