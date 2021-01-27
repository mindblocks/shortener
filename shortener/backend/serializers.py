from rest_framework import serializers
from backend.models import Shortener

# Lead Serializer
class ShortenerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shortener
    fields = '__all__'

