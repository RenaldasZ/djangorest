from rest_framework import serializers
from . import models

class SongListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'band']


class BandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ['id', 'name', 'picture']


class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = serializers.StringRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
 
    def get_comment_count(self, obj):
        return models.SongReviewComment.objects.filter(song_review=obj).count()
    
    def get_likes_count(self, obj):
        return models.SongReviewLike.objects.filter(song_review=obj).count()

    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'user_id', 'song', 'content', 'score', 'comment_count', 'likes_count', 'comments']


class SongReviewLikesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.SongReviewLike
        fields = ['id']


class SongReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    song_review = serializers.ReadOnlyField(source='song_review.id')

    class Meta:
        model = models.SongReviewComment
        fields = ['id', 'user', 'user_id', 'song_review', 'content']

