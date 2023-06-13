from rest_framework import serializers
from . import models

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'band']