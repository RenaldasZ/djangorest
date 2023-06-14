from rest_framework import serializers
from . import models

class SongListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'band']


class BandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ['id', 'name']


class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'user_id', 'song', 'content', 'score']