from rest_framework import serializers

from tumordetection.models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'image']