from rest_framework import serializers
from ..models import Sook

class SookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sook
        fields = '__all__'

class SookRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sook
        fields = '__all__'

class SookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sook
        fields = '__all__'